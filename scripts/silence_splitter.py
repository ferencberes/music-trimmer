import sys
from pydub import AudioSegment
from pydub.silence import split_on_silence

def split_song(f_name, length_val, threshold_val, overwrite=True, export_all=False):
	f_prefix = f_name[0:-4]
	sound = AudioSegment.from_mp3(f_name)
	print '%s was loaded.' % f_name
	print 'Splitting by silence STARTED.'
	chunks = split_on_silence(sound, min_silence_len=length_val, silence_thresh=-threshold_val)
	print 'Splitting by silence FINISHED.'
	if not len(chunks)==1:
		if export_all:
			for i, chunk in enumerate(chunks):
				chunk.export('%s_part_%i.mp3' % (f_prefix, i), format="mp3")
			print 'Segments were saved to %i mp3 files.' % len(chunks)
		else:
			if overwrite:
				chunks[0].export(f_name, format="mp3")
			else:
				chunks[0].export('%s_part_0.mp3' % f_prefix, format="mp3")
		print 'Splitting %s DONE' % f_name
	else:
		print 'No splitting was needed for %s!' % f_name

if __name__ == '__main__':
	argc = len(sys.argv)
	if argc >= 4:
		f_name = sys.argv[1]
		min_silence_length=int(sys.argv[2]) # 500
		silence_threshold= int(sys.argv[3]) # 26
		if argc == 5:
			split_song(f_name, min_silence_length, silence_threshold, bool(sys.argv[4]))
		else:
			split_song(f_name, min_silence_length, silence_threshold)
	else:
		print 'Usage: <file_name> <min_silence_length> <silence_threshold> <export_all>'