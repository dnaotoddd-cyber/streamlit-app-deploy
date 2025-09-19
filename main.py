
print("Hello VSCode!")


fruit_list = ["apple", "banana", "cherry"]
# リストから偶数だけを抽出する関数
def extract_even_numbers(input_list):
    return [num for num in input_list if num % 2 == 0]

# 関数「extract_even_numbers」に要素数が10のリストを渡して、戻り値のリストの合計値と平均値を計算して表示する
numbers = list(range(1, 11))
even_numbers = extract_even_numbers(numbers)
print("Even numbers:", even_numbers)
print("Sum:", sum(even_numbers))
print("Average:", sum(even_numbers) / len(even_numbers) if even_numbers else 0)

# 数値のリストを受け取り、各値に基づいてカテゴリを分類する関数を作成してください

# 条件:

# 1. 値が0以下の場合は "Low" カテゴリに分類してください

# 2. 値が1以上10以下の場合は "Medium" カテゴリに分類してください

# 3. 値が10を超える場合は "High" カテゴリに分類してください

# 4. 入力リストには整数が含まれるものとします

# 結果を辞書形式で返してください。キーがカテゴリ名で、値が該当する数値のリストとします


def calculate_bmi(weight, height):
    """BMIを計算する関数"""
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    bmi = weight / (height ** 2)
    return bmi
# BMIを計算する関数

# BMIを表示してから戻り値を返す

def calculate_bmi
def calculate_bmi(weight, height):
    """BMIを計算する関数"""
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.2f}")
    return bmi
person = {"name": "山田太郎", "age": 30, "prefecture": "東京都"}
person["job"] = "エンジニア"

for key, value in person.items():

    print(f"{key}: {value}")(weight, height):