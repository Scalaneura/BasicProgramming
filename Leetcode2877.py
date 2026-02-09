import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:

    column_names = ["student_id","age"]
    df = pd.DataFrame(student_data, columns=column_names)
    return df

    data = [
        [1, 15],
        [2, 11],
        [3, 11],
        [4, 20]
    ]

    df_result = createDataframe(data)
    print(df_result)
