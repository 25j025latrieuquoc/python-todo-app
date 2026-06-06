

import json
try:
    with open ("tasks.json","r",encoding = "utf-8") as file:
        tasks = json.load(file)
except:
    tasks =[]
def save_tasks():
    with open ("tasks.json","w",encoding = "utf-8") as file:
        json.dump(tasks,file,ensure_ascii = False, indent = 4)




#tasks = [] # 　タスクを作成, 毎回毎回実行すること新規のリスト作成する

while True: # メニューの選択リスクを作って、表示 
    print("本日の実施予定")

    print ("1.やる事入力")
    print ("2.リスト表す")
    print ("3.終了する")
    print ("4.削除")
    print ("5.完了チェック")

    choice = input("選択:")
            #　１を選択したら、やる事を入力/
          
    if choice =="1":
        task = input("やる事を入力してください")

        tasks.append({
            "name":task, #入力されたのやる事
            "done":False #完了しない／した状態


        })
        save_tasks()
        print ("追加されました",task)

        
    elif choice =="2":   #２を選択したら、入力されたデータが表示します
        print("やる事のリスク: ")
        for i, task in  enumerate(tasks):
            # i は　enumerateが作成したインデックス。
            #  enumerateを使うことで、インデックスと要素を同時に取得できます。
                
            if task["done"] == True:
                print ( i+1,"[x]",task["name"])
            else:
                print (i+1,"[ ]",task["name"])
      


    elif choice == "3": 
        break

    elif choice == "4":
        task = int(input ("削除したい番号を入力"))
        print ("消しました‼",tasks[task-1])
        del tasks[ task-1 ]
        save_tasks()


    elif choice == "5":
        number = int (input("番号入力:"))
        tasks[number -1]["done"] = True    
        save_tasks()   
        # lay phan tu thu  number -1 trong list       
        # #truy cap key done trong dict do
        #doi tu false sang true 

        print (" 完了しました。")
        
        
    else:
        print("エラー発生、", 
              
              "再入力してください")
        
