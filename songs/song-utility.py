import sys
import dataclasses

@dataclasses.dataclass
class Song():
    name : str
    delay_first : int
    bpm : int
    note_num : int
    notes : list

@dataclasses.dataclass
class Note():
    number : int
    column : int
    delay : float

def loadnotes(path):
    with open(path, "r") as f:
        song_name = f.readline().strip()
        delay_first = int(f.readline())
        bpm = int(f.readline())
        note_num = int(f.readline())

        notes = []

        for line in f:
            if len(line) <= 1:
                continue
            else:
                split = line.split()           
                notes.append( Note(number=int(split[0]), column=int(split[1]), delay=float(split[2])) )

        return Song(song_name, delay_first, bpm, note_num, notes)

def times_to_abs(song : Song):
    cur_time = song.delay_first
    abs_times = []
    for note in song.notes:
        abs_times.append(cur_time)
        cur_time += note.delay
    return abs_times


def main(args):
    if len(args) > 0:
        path = args[0]
        song = loadnotes(path)
        abs_times = times_to_abs(song)
        path_split = path.split('.')
        with open( ''.join([path_split[0],"_abs.txt"]) , "w") as f:
            for time in abs_times:
                f.write(str(time) + "\n")

if __name__ == "__main__":
    main(sys.argv[1:])