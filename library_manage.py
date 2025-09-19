def list_all_borrow_records():
    print("--- 全ての貸出履歴 ---")
    if not borrow_records:
        print("貸出履歴はありません。")
        return
    for record in borrow_records:
        book = next((b for b in books if b["book_id"] == record["book_id"]), None)
        member = next((m for m in members if m["member_id"] == record["member_id"]), None)
        book_title = book["title"] if book else "不明"
        member_name = member["name"] if member else "不明"
        status = "返却済み" if record["returned"] else "貸出中"
        print(f"図書: {book_title}（ID: {record['book_id']}）, 会員: {member_name}（ID: {record['member_id']}）, 貸出日: {record['borrow_date']}, 返却期限: {record['due_date']}, 状態: {status}")
books = []
members = []
borrow_records = []

def add_book(book_id, title, author, copies):
    for b in books:
        if b["book_id"] == book_id:
            print(f"図書ID「{book_id}」の本は既に存在します。")
            return
    books.append({
        "book_id": book_id,
        "title": title,
        "author": author,
        "copies": copies,
        "available_copies": copies
    })
    print(f"図書「{title}」（ID: {book_id}, 著者: {author}, 冊数: {copies}）を追加しました。")

def list_books():
    if not books:
        print("現在、登録されている図書はありません。")
        return
    print("--- 図書一覧 ---")
    for b in books:
        print(f"ID: {b['book_id']}, タイトル: {b['title']}, 著者: {b['author']}, 総冊数: {b['copies']}, 在庫: {b['available_copies']}")

def search_book(book_id):
    for b in books:
        if b["book_id"] == book_id:
            print(f"ID: {b['book_id']}, タイトル: {b['title']}, 著者: {b['author']}, 総冊数: {b['copies']}, 在庫: {b['available_copies']}")
            return
    print(f"図書ID「{book_id}」の本は存在しません。")

def add_member(member_id, name):
    for m in members:
        if m["member_id"] == member_id:
            print(f"会員ID「{member_id}」の会員は既に存在します。")
            return
    members.append({"member_id": member_id, "name": name})
    print(f"会員「{name}」（ID: {member_id}）を追加しました。")

def list_members():
    if not members:
        print("現在、登録されている会員はいません。")
        return
    print("--- 会員一覧 ---")
    for m in members:
        print(f"ID: {m['member_id']}, 名前: {m['name']}")

def borrow_book(book_id, member_id):
    book = None
    for b in books:
        if b["book_id"] == book_id:
            book = b
            break
    if not book:
        print(f"図書ID「{book_id}」の本は存在しません。")
        return
    member = None
    for m in members:
        if m["member_id"] == member_id:
            member = m
            break
    if not member:
        print(f"会員ID「{member_id}」の会員は存在しません。")
        return
    if book["available_copies"] <= 0:
        print(f"図書「{book['title']}」は現在貸出可能な冊数がありません。")
        return
    record_count = sum(1 for r in borrow_records if r["member_id"] == member["member_id"])
    if record_count >= 5:
        print(f"貸出可能数は5冊までです。")
        return
    borrow_records.append({
        "book_id": book_id,
        "member_id": member_id,
        "borrow_date": "2024-11-24",
        "due_date": "2024-12-01",
        "returned": False
    })
    print(f"図書「{book['title']}」を会員「{member['name']}」に貸し出しました。\n返却期限: 2024-12-01")
    book["available_copies"] -= 1

def list_borrowed_books():
    print("--- 貸出中の図書一覧 ---")
    borrow_count = 0
    for r in borrow_records:
        if not r["returned"]:
            book = next((b for b in books if b["book_id"] == r["book_id"]), None)
            member = next((m for m in members if m["member_id"] == r["member_id"]), None)
            book_title = book["title"] if book else "不明"
            member_name = member["name"] if member else "不明"
            print(f"図書: {book_title}（ID: {r['book_id']}）, 会員: {member_name}（ID: {r['member_id']}）, 貸出日: {r['borrow_date']}, 返却期限: {r['due_date']}")
            borrow_count += 1
    if borrow_count == 0:
        print("現在、貸出中の図書はありません。")

def return_book(book_id, member_id):
    record = None
    for r in borrow_records:
        if r["book_id"] == book_id and r["member_id"] == member_id and not r["returned"]:
            r["returned"] = True
            record = r
            break
    if not record:
        print(f"図書ID「{book_id}」本を会員ID「{member_id}」の会員は借りていません。")
        return
    book = next((b for b in books if b["book_id"] == book_id), None)
    if book:
        book["available_copies"] += 1
        print(f"図書「{book['title']}」が返却されました。")
    else:
        print(f"図書ID「{book_id}」の本は存在しません。")

def calculate_fines():
    print("--- 延滞料金一覧 ---")
    found = False
    for r in borrow_records:
        if not r["returned"]:
            book = next((b for b in books if b["book_id"] == r["book_id"]), None)
            member = next((m for m in members if m["member_id"] == r["member_id"]), None)
            due_date = "2024-12-01"
            today = "2024-12-24"
            overdue_days = max((int(today[-2:]) - int(due_date[-2:])), 0)
            fine = overdue_days * 100
            book_title = book["title"] if book else "不明"
            member_name = member["name"] if member else "不明"
            print(f"図書: {book_title}（ID: {r['book_id']}）, 会員: {member_name}（ID: {r['member_id']}）, 延滞料金: {fine}円")
            found = True
    if not found:
        print("現在、貸出中の図書はありません。")

def main():
    while True:
        print("図書館管理システムメニュー:")
        print("1: 図書を追加")
        print("2: 図書一覧を表示")
        print("3: 図書を検索")
        print("4: 会員を追加")
        print("5: 会員一覧を表示")
        print("6: 図書を貸し出す")
        print("7: 貸出中の図書一覧を表示")
        print("8: 図書を返却")
        print("9: 延滞料金を計算")
        print("10: 終了")

        try:
            choice = int(input("操作を選択してください（1-10）: "))

            if choice == 1:
                book_id = input("図書IDを入力してください: ")
                title = input("タイトルを入力してください: ")
                author = input("著者名を入力してください: ")
                copies = int(input("冊数を入力してください: "))
                add_book(book_id, title, author, copies)

            elif choice == 2:
                list_books()

            elif choice == 3:
                search_book()

            elif choice == 4:
                member_id = input("会員IDを入力してください: ")
                name = input("名前を入力してください: ")
                add_member(member_id, name)

            elif choice == 5:
                list_members()

            elif choice == 6:
                book_id = input("貸し出す図書IDを入力してください: ")
                member_id = input("会員IDを入力してください: ")
                borrow_book(book_id, member_id)

            elif choice == 7:
                list_borrowed_books()

            elif choice == 8:
                book_id = input("返却する図書IDを入力してください: ")
                member_id = input("会員IDを入力してください: ")
                return_book(book_id, member_id)

            elif choice == 9:
                calculate_fines()

            elif choice == 10:
                print("図書館管理システムを終了します。")
                break

            else:
                print("無効な選択です。1-10の数字を入力してください。")

        except ValueError as e:
            print(f"入力エラー: {e}")
        except Exception as e:
            print(f"予期しないエラーが発生しました: {e}")

main()