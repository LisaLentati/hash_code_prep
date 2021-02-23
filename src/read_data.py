import sys

def read_data(file_url):

    my_file = open(file_url, "r")

    info_line = [int(x) for x in my_file.readline().strip().split()]

    # n_cols = info_line[0]
    # n_rows = info_line[1]
    # n_arms = info_line[2]
    # n_mnts = info_line[3]
    # n_tasks = info_line[4]
    # n_steps = info_line[5]

    # mounts_pos = dict()
    # for i in range(n_mnts):
    #     line = [int(x) for x in my_file.readline().strip().split()]
    #     mounts_pos[i] = (line[0], line[1])

    # tasks_pos = dict()
    # tasks_val = dict()
    # for i in range(n_tasks): 
    #     line = [int(x) for x in my_file.readline().strip().split()]
    #     tasks_val[i] = line[0]
    #     n_assembly_points = line[1]
    #     line = [int(x) for x in my_file.readline().strip().split()]
    #     list_assembly_points = list()
    #     for j in range(n_assembly_points):
    #         list_assembly_points.append((line[2*j],line[2*j+1]))
    #     tasks_pos[i] = list_assembly_points

    my_file.close
    return info_line








# if __name__ == '__main__':
url = '../data/d_many_pizza.in'
a = read_data(url)
#print(a)

print(sys.path)