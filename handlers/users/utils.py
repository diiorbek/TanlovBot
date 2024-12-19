import sqlite3
import matplotlib.pyplot as plt
from loader import hokim_list, bank_list, boshqarma_list, quruvchi_list

connection = sqlite3.connect("votes.db")

def add_vote(full_name, user_id, table_name, user_select):
    connection = sqlite3.connect("votes.db")
    
    try:
        command = f"""
INSERT INTO '{table_name}'
VALUES(?, ?, ?);
    """
    
        cursor = connection.cursor()
        cursor.execute(command, (full_name, user_id, user_select))

        connection.commit()
        return "Ovozingiz qabul qilindi!"

    except:
        return "Siz allaqachon ovoz bergansiz!"


def get_votes_for_table(table_name, data_list):
    conn = sqlite3.connect('votes.db')
    cursor = conn.cursor()
    votes = {}
    total_votes = 0
    
    for name in data_list:
        query = f"SELECT COUNT(*) FROM `{table_name}` WHERE user_select = ?"
        cursor.execute(query, (name,))
        count = cursor.fetchone()[0]
        votes[name] = count
        total_votes += count
    
    conn.close()
    
    try:
        percentages = [count / total_votes * 100 for count in votes.values()]
    except ZeroDivisionError:
        percentages = [0] * len(votes.values()) 
    
    return votes, percentages

def create_statistics_images():
    import os
    if not os.path.exists('statistics'):
        os.makedirs('statistics')  

    data_lists = {
        "hokim": hokim_list,
        "bank": bank_list,
        "boshqarma": boshqarma_list,
        "quruvchi": quruvchi_list
    }

    statistics = {}

    for table_name, data_list in data_lists.items():
        votes, percentages = get_votes_for_table(table_name, data_list)
        if not votes:
            continue  

        plt.figure(figsize=(12, 8))
        bars = plt.bar(data_list, percentages, color=plt.cm.Paired.colors[:len(percentages)], edgecolor='black')
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, yval + 1, f'{yval:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

        plt.ylabel('Ovozlar foizi', fontsize=12)
        plt.title(f'Diagramma: {table_name} (Foiz)', fontsize=16)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.tight_layout()

        plt.savefig(f'statistics/{table_name}_statistics.png')
        plt.close()

        statistics[table_name] = "\n".join([f"{name}: {count}" for name, count in votes.items()])

    return statistics

def get_statistics(name, table_name, lst):
    res = get_votes_for_table(table_name, lst)[0][name]
    
    return res


def write_probel(word):
    if len(word) < 39:
        word += (39 - len(word)) * " "
        
    return word
