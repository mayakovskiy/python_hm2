def g(df):
    unique_values = df['whoAmI'].unique()

    # Создаем пустой DataFrame
    one_hot_df = pd.DataFrame()

    for value in unique_values:
        # Создаем новый столбец с именем, равным значению
        one_hot_df[value] = df['whoAmI'].apply(lambda x: 1 if x == value else 0)

    return one_hot_df

# Применяем функцию к нашему DataFrame
one_hot_df = g(data.copy())

# Проверяем результат
one_hot_df.head()
