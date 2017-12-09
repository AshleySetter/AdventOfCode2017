from glob import glob

python_files = sorted(glob('day*/*/part*.py'))
cpp_files = sorted(glob('day*/*/part*.cpp'))

cpp_opt_levels = ['O0', 'O1', 'O2', 'O3']

singlebackstring = '../'
with open('timefiles.sh', 'w') as writefile:
    for day in range(1, 26):
        daystring = 'day{}'.format(day)
        pyfiles = [filepath for filepath in python_files if daystring in filepath]
        cppfiles = [filepath for filepath in cpp_files if daystring in filepath]
        for filepath in pyfiles:
            if 'part1' in filepath:
                dirname = filepath[:-9]
                filename = filepath.split('/')[-1]
                backamount = len(filepath.split('/')) - 1
                backstring = backamount * singlebackstring
                writefile.write('cd {}\n'.format(dirname))
                writefile.write('time python {}\n'.format(filename))
                writefile.write('cd {}\n'.format(backstring))
        for filepath in cppfiles:
            if 'part1' in filepath:
                dirname = filepath[:-9]
                filename = filepath.split('/')[-1][:-4]
                backamount = len(filepath.split('/')) - 1
                backstring = backamount * singlebackstring
                optruns = [filename + opt_lvl for opt_lvl in cpp_opt_levels]
                writefile.write('cd {}\n'.format(dirname))
                for run in optruns:
                    writefile.write('time ./{}\n'.format(run))
                writefile.write('cd {}\n'.format(backstring))

        for filepath in pyfiles:
            if 'part2' in filepath:
                dirname = filepath[:-9]
                filename = filepath.split('/')[-1]
                backamount = len(filepath.split('/')) - 1
                backstring = backamount * singlebackstring
                writefile.write('cd {}\n'.format(dirname))
                writefile.write('time python {}\n'.format(filename))
                writefile.write('cd {}\n'.format(backstring))
        for filepath in cppfiles:
            if 'part2' in filepath:
                dirname = filepath[:-9]
                filename = filepath.split('/')[-1][:-4]
                backamount = len(filepath.split('/')) - 1
                backstring = backamount * singlebackstring
                optruns = [filename + opt_lvl for opt_lvl in cpp_opt_levels]
                writefile.write('cd {}\n'.format(dirname))
                for run in optruns:
                    writefile.write('time ./{}\n'.format(run))
                writefile.write('cd {}\n'.format(backstring))
