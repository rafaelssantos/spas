import numpy
import score_functions






def load_labels(file_path):
    file = open(file_path, 'r')
    lines = file.readlines()
        

    feature_labels = []

    for line in lines:
        feature_labels.append(line.strip())
    
    return feature_labels





def load_data(file_path):
    data = numpy.loadtxt(file_path, delimiter=',')
    return data





def calc_scores(feature_data):
    labels = []
    labels.append('Laplacian')

    data = []
    # scores.calc_lap_score(feature_data)
    data.append(score_functions.calc_lap_score(feature_data))

    return data, labels





def generate_dict(feature_labels, score_labels, score_data, title=''):
    values_keys = list(score_labels)
    values_keys.insert(0, 'name')
    json = []
    values = []

    for i in range(0, len(score_data), 1):
        values.append(score_data[i].tolist())
        json_score_line = score_data[i].tolist()
        json_score_line.insert(0, feature_labels[i])
        json.append(dict(zip(values_keys, json_score_line)))

    result_dict = {}
    result_dict['scoreLabels'] = score_labels
    result_dict['featureLabels'] = feature_labels
    result_dict['title'] = title
    result_dict['values'] = values
    result_dict['json'] = json

    return result_dict

