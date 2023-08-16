import figure_util


figure_util.Draw(
    figureTitle="MySQL vs WeSQL-Scale (With Read Write Split Disable)",
    configs=[
        {
            'barName': 'MySQL',
            'lineName': 'MySQL Latency',
            'fileName': './data/mysql-disable.csv',
        },
        {
            'barName': 'WeSQL-Scale',
            'lineName': 'WeSQL-Scale Latency',
            'fileName': './data/vtgate-disable.csv',
        },
    ]
)


figure_util.Draw(
    figureTitle="MySQL vs WeSQL-Scale (With Read Write Split Enable)",
    configs=[
        {
            'barName': 'MySQL',
            'lineName': 'MySQL Latency',
            'fileName': './data/mysql-enable.csv',
        },
        {
            'barName': 'WeSQL-Scale',
            'lineName': 'WeSQL-Scale Latency',
            'fileName': './data/wesql-scale-enable.csv',
        },
    ]
)
