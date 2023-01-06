import time
questions = [
    ["Name the Father of the Indian Constitution?", "Mahatma Gandhi", "Jawaharlal Nehru", "B.R.Ambedkar", "Rajendra Prasad",3],
    ["Name the deepest ocean in the world?", "Pacific", "Atlantic", "Indian", "Arctic", 1],
    ["Name the gas which is filled in balloons?", "Nitrogen", "Helium", "Oxygen", "Argon", 2],
    ["Aizawl is the capital of which state of India?", "Arunachal Pradesh", "Assam", "Manipur", "Mizoram", 4],
    ["Who is the executive head of the Union Territories?", "President", "Chief Minister", "Prime Minister", "Governor", 1],
    ["How many Union Territories are there in India?", "6", "7", "8", "9", 3],
    ["Where is Gir National Forest located?", "Rajasthan", "Gujrat", "Madhya Pradesh", "Uttarakhand", 2],
    ["Which planet is closest to the Sun?", "Mars", "Earth", "Mercury", "Venus", 3],
    ["1024 Kilobytes is equal to", "1 Megabyte", "1 Terabyte", "1 Gigabye", "1 Byte", 1],
    ["Delhi is situated on the bank of which river?", "Ganga", "Yamuna", "Saraswati", "Godavari", 2],
    ["Victoria Memorial is situated in which city of India?", "Kolkata", "Delhi", "Bangalore", "Chennai", 1],
    ["Which city is called Pearl City?", "Delhi", "Ahmedabad", "Lucknow", "Hyderabad", 4],
    ["Who penned the book 'Wings of Fire'?", "Apj Abdul Kalam", "Subhas Chandra Bose", "Bhagat Singh", "Aurobindo Ghosh", 1],
    ["Name the summer capital of Jammu and Kashmir?", "Kashmir", "Jammu", "Srinagar", "Dal", 3],
    ["Which day is celebrated as Environment Day?", "5 June", "5 July", "5 August", "10 August", 1],
]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0
try:
    print("===Welcome to the Quiz Game===\n")
    time.sleep(1.5)
    for i in range(0,len(questions)):
        question = questions[i]
        print("============================")
        print(f"Question for Rs. {levels[i]}\n")
        print(f"Q{i+1}. {question[0]}")
        print(f"1. {question[1]}      2. {question[2]}")
        print(f"3. {question[3]}      4. {question[4]}")
        reply = int(input("\nEnter your choice between 1 to 4. To quit, press 0 :\n"))
        time.sleep(0.7)
        if reply == question[-1]:
            print(f"\nCorrect answer. You have won Rs. {levels[i]}.")
            print("============================\n")
            time.sleep(2)
            if i == 4:
                money = 10000
            elif i == 9:
                money = 320000
            elif i == 14:
                money = 10000000
        elif reply == 0:
            money = levels[i-1]
            break
        elif reply > 4:
            print("Wrong input. Closing the program now. Restart the program to play again.")
            break
        else:
            print("Oops! Wrong answer. Game over")
            break
except Exception:
    print("Wrong input. Closing the program now. Restart the program to play again.")
print(f"Thank you for playing. You won Rs. {money}.")