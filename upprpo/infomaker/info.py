import pickle


def main():
    data1 = {'Model': 'court of law', 'agent': 'complainant', 'opponent': 'Judge', 'goal': ['get evidence'],
             'plan': ['request investigation', 'conduct investigation', 'get evidence'], 'missing': ['evidence'], 'time': 'T'}
    data2 = {'court of law': {'agents': ['complainant', 'Judge'], 'conflict': 'need for extra investigation', 'previous decisions': [],
                              'possible agent1 arguments': ['arg1'], 'possible agent2 arguments': ['arg2']},
             'selling a car': {'agents': ['customer', 'seller'], 'conflict': 'the absence of payment', 'previous decisions': ['customer is forsed to pay']} }
    with open('../dialog/case.pkl', 'wb') as f1:
        pickle.dump(data1, f1)
    f1.close()
    with open('../dialog/Models.pkl', 'wb') as f2:
        pickle.dump(data2, f2)
    f2.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
