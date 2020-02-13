import numpy as np

list_instance_class0 = []
list_instance_class1 = []


def generate_list_instance(filename):
    with open(filename) as fp:
        num_att = 0
        is_first_line = True
        for line in fp.readlines():
            tokens = line.split(",")

            # get the num of instance and attribute
            if is_first_line:
                is_first_line = False
                num_att = int(tokens[1])
                continue
            # get the temp instance
            temp_instance = []
            for i in range(num_att):
                temp_instance.append(float(tokens[i]))
            # append to the class'es list
            belonging_class = int(tokens[num_att])
            if belonging_class == 0:
                list_instance_class0.append(temp_instance)
            else:
                list_instance_class1.append(temp_instance)


def calculate_f_value():
    max_f_value = 0
    num_att = len(list_instance_class0[0])
    narray_class0 = np.array(list_instance_class0)
    narray_class1 = np.array(list_instance_class1)
    list_mean_class0 = np.mean(narray_class0, axis=0)
    list_mean_class1 = np.mean(narray_class1, axis=0)
    list_var_class0 = np.var(narray_class0, axis=0)
    list_var_class1 = np.var(narray_class1, axis=0)
    for i in range(num_att):
        mean_c0 = list_mean_class0[i]
        mean_c1 = list_mean_class1[i]
        var_c0 = list_var_class0[i]
        var_c1 = list_var_class1[i]
        current_f_value = (mean_c0 - mean_c1) * (mean_c0 - mean_c1) / (var_c0 + var_c1)
        if max_f_value < current_f_value:
            max_f_value = current_f_value

    return max_f_value


def calculate_f_value_average():
    list_f_value = []
    num_att = len(list_instance_class0[0])
    narray_class0 = np.array(list_instance_class0)
    narray_class1 = np.array(list_instance_class1)
    list_mean_class0 = np.mean(narray_class0, axis=0)
    list_mean_class1 = np.mean(narray_class1, axis=0)
    list_var_class0 = np.var(narray_class0, axis=0)
    list_var_class1 = np.var(narray_class1, axis=0)
    for i in range(num_att):
        mean_c0 = list_mean_class0[i]
        mean_c1 = list_mean_class1[i]
        var_c0 = list_var_class0[i]
        var_c1 = list_var_class1[i]
        current_f_value = (mean_c0 - mean_c1) * (mean_c0 - mean_c1) / (var_c0 + var_c1)
        list_f_value.append(current_f_value)

    return float(sum(list_f_value)) / len(list_f_value)


if __name__ == '__main__':
    with open("f_value.txt", 'w') as fp_w:
        list_name_ds = ["appendicitis", "wdbc", "sonar", "ionosphere", "spectfheart", "australian", "flare-solar",
                        "pima", "saheart", "heart", "monks", "bupa", "haberman", "page-blocks-2class(major_0)"]
        for i in range(len(list_name_ds)):
            filename_tra = "./datasets/a0_0_" + list_name_ds[i] + "-10tra.dat"
            filename_tst = "./datasets/a0_0_" + list_name_ds[i] + "-10tst.dat"
            generate_list_instance(filename_tra)
            generate_list_instance(filename_tst)
            fp_w.write(list_name_ds[i] + " : " + str(calculate_f_value()) + "\n")
            list_instance_class0.clear()
            list_instance_class1.clear()
    # with open("f_value_average.txt", 'w') as fp_w:
    #     list_name_ds = ["appendicitis", "wdbc", "sonar", "ionosphere", "spectfheart", "australian", "flare-solar",
    #                     "pima", "saheart", "heart", "monks", "bupa", "haberman", "page-blocks-2class(major_0)"]
    #     for i in range(len(list_name_ds)):
    #         filename_tra = "./datasets/a0_0_" + list_name_ds[i] + "-10tra.dat"
    #         filename_tst = "./datasets/a0_0_" + list_name_ds[i] + "-10tst.dat"
    #         generate_list_instance(filename_tra)
    #         generate_list_instance(filename_tst)
    #         fp_w.write(list_name_ds[i] + " : " + str(calculate_f_value_average()) + "\n")
    #         list_instance_class0.clear()
    #         list_instance_class1.clear()
