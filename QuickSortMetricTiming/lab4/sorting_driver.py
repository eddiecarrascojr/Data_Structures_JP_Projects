import os
from lab4.uti import read_the_file
from lab4.quicksort import Iterative_Quick_Sort_Version_1, Iterative_Quick_Sort_Version_2, Iterative_Quick_Sort_Version_3, Iterative_Quick_Sort_Version_4

#Driver code
if __name__ == '__main__':
    print('Code Running As Expected')

    #search for .txt files and append to list
    all_files = []
    for files in os.listdir():
        if files.endswith('.txt'):
            all_files.append(files)
        else:
            continue
    split_files = []
    for file in all_files:
        split_file = file.split('_')
        split_file = split_file[:-1]
        split_file[1] = int(split_file[1])
        split_files.append(split_file)

    sorted_files = sorted(split_files, key=lambda x: (x[0], x[1]))

    for file_data in sorted_files:
        file_type = file_data[0]
        file_size = file_data[1]
        file_name = file_type + '_' + str(file_size) + '_' + 'Character.txt'
        file_out = file_type + '_' + str(file_size)  + '_Output.txt'


        #For quicksort version 1:
        array = read_the_file(file_name)

        print('File Name: ', file_name,'...................................................')

        with open(file_out, 'a') as path:
            print('File Name: ', file_name,'...................................................' ,file=path)

        function_list = [Iterative_Quick_Sort_Version_1(array, array.index(array[0]), array.index(array[-1])),
                         Iterative_Quick_Sort_Version_2(array, array.index(array[0]), array.index(array[-1])),
                         Iterative_Quick_Sort_Version_3(array, array.index(array[0]), array.index(array[-1])),
                         Iterative_Quick_Sort_Version_4(array, array.index(array[0]), array.index(array[-1]))]

        version = 0
        for function in function_list:
            version += 1
            with open(file_out, 'a') as path:
                print('Sort Function: Version', version, file=path)
                #print to file
                if len(array) == 50:
                    print('Sorted Array: ', function[-3], file=path)
                print('Swap Count: ', function[-2], file=path)
                print('Comparison Count: ', function[-1], file=path)
                print('\n', file=path)