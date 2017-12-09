import subprocess

subprocess.call(["./timefiles.sh &> output.txt"], shell=True)

day = 1
part = 1
language = ['c++ [-O0]', 'c++ [-O1]', 'c++ [-O2]', 'c++ [-O3]', 'Python']
NumRepeats = 1000

counter = 0

times = []

with open('output.txt') as infile:
    temp = []
    for line in infile:
        if 'real' in line:            
            result = line.split('\t')[1].split('m')
            mins = float(result[0])
            seconds = float(result[1].split('s')[0])
            print('day {}, part {}'.format(day, part))
            print('language: {}'.format(language[counter]))
            mins_in_secs = mins * 60
            seconds += mins_in_secs
            seconds_per_run = seconds/NumRepeats
            print('seconds: {:e}'.format(seconds_per_run))
            temp.append(seconds_per_run)
            counter += 1
            if counter >= len(language):
                times.append([day, part] + temp)
                temp = []
                counter = 0
                if part == 2:
                    part = 1
                    day += 1
                else:
                    part += 1

for i, daypart in enumerate(times):
    for j, number in enumerate(daypart):
        if j > 1:
            times[i][j] = '{:g}μs'.format(number/1e-6)
        else:
            times[i][j] = '{:d}'.format(number)

print(times)
        
with open('README.md', 'w') as readme_file:
    with open('README_template.md', 'r') as template_file:
        for line in template_file:
            readme_file.write(line)
    for daypart in times:                    
        stringtimes = str(daypart)
        stringtimes = stringtimes.replace(',', '|')
        stringtimes = stringtimes.replace(']', '|')
        stringtimes = stringtimes.replace('[', '|')
        stringtimes = stringtimes.replace("'", ' ')
        readme_file.write(stringtimes+'\n')
