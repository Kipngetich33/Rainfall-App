def list_city_rainfalls(data):
    amounts = []
    for item in data:
        amounts.append(item.amount)
    return amounts

def create_labels(data):
    labels = []
    for item in data:
        labels.append(item.city)
    return labels

def assign_colors(data):
    chosen_colors = []
    background_colors =['rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
    ]
    for i in range(0,data):
        position = i % 6
        chosen_colors.append(background_colors[position])
    return chosen_colors

def assign_borders(data):
    chosen_colors = []
    background_colors =['rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
    ]
    for i in range(0,data):
        position = i % 6
        chosen_colors.append(background_colors[position])
    return chosen_colors

