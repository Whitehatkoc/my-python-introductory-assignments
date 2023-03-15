# Sümeyra Koç  2210765020
import sys
with open("Battleship.out","w") as out_file:   # these two lines are to delete the outputs of the previous game when the game starts from the beginning.
    out_file.write("")

# let's check if entered files are proper.
out_file=open("Battleship.out","a")
oyun = True
while True:
    erorlu_dosyalar_listesi = []
    try:
        for y in range(5):
            try:
                with open(sys.argv[y], "r"):
                    pass
            except IOError:
                erorlu_dosyalar_listesi.append(sys.argv[y])
                oyun = False
    except IndexError:
        print("the number of files you entered is missing !")
        out_file.write("the number of files you entered is missing !\n")
        oyun = False
    except:
        print("there is an error in the files you entered, please try again.")
        out_file.write("there is an error in the files you entered, please try again.\n")
        oyun = False
    if len(erorlu_dosyalar_listesi) > 0:
        string_hali = " ".join(erorlu_dosyalar_listesi)
        print(f"IOError: {string_hali} is/are not reachable")
        out_file.write(f"IOError: {string_hali} is/are not reachable\n")
    break
out_file.close()

# let's start to our code !!!!

if oyun:
    ord_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
                "J"]  # bu liste sadece girilen hamlenin harf olması gerken kısmın harf olup olmadığını kontrol etmek için.
    main_list_player1, main_list_player2 = [["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"] for y in range(10)], [
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"] for z in range(10)]
    print("^-^ Battle of Ships Game ^-^\n")

    player_1_hidden_board, player_2_hidden_board = [["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"] for y in
                                                    range(10)], [["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"] for
                                                                 z in range(10)]
    dic = {}
    roundd = 1
    gemi_listesi = ["Carrier", "Battleship", "Destroyer", "Submarine", "Patrol Boat"]

    out_file = open("Battleship.out", "a", encoding="utf-8") # I'll close the file the next time the game ends
    out_file.write("^-^ Battle of Ships Game ^-^\n\n")
    def printt(p, e, hangi1, hangi2):
        if hangi1 == player_1_hidden_board and hangi2 == player_2_hidden_board and draw_or_not == False: # eğer burası True ise oyundayız demektir, eğer false ise oyun sona ermiş demektir.
            print(f"Player{p}'s Move\n")
            out_file.write(f"Player{p}'s Move\n\n")          # "Battleship.i use two "\n" signs when printing to the "out" file, because one is to switch to a lower line,
            print(f"Round :{roundd:<21}\tGrid Size: 10x10\n")  # the other is to put a space from the falsa to prevent the text from being at the bottom
            out_file.write(f"Round :{roundd:<21}\tGrid Size: 10x10\n\n")
            print(f"Player1's Hidden Board\t\tPlayer2's Hidden Board\n")
            out_file.write(f"Player1's Hidden Board\t\tPlayer2's Hidden Board\n\n")
        alp_list = [chr(y + 65) for y in range(10)]
        b = " ".join(alp_list)
        print(f"{b:>21}\t\t{b:>21}")
        out_file.write(f"{b:>21}\t\t{b:>21}\n")
        for x in range(10):
            a = " ".join(hangi1[x])
            print(f"{x + 1:<2}" + a, "\t\t", end="")

            out_file.write(f"{x + 1:<2}" + a+ " \t\t")
            b = " ".join(hangi2[x])
            print(f"{x + 1:<2}" + b)
            out_file.write(f"{x + 1:<2}" + b+"\n")
        print("\n")
        out_file.write("\n")
        if hangi1 == player_1_hidden_board and hangi2 == player_2_hidden_board and draw_or_not == False:
            for x in gemi_listesi:
                returnn1 = information(x[0], 1)
                returnn2 = information(x[0], 2)
                print(f"{x:<15}{returnn1}\t\t{x:<15}{returnn2}")
                out_file.write(f"{x:<15}{returnn1:<8}\t\t{x:<15}{returnn2}\n")
            print(f"\nEnter your move: {e}\n")
            out_file.write(f"\nEnter your move: {e}\n\n")


    # let's prepare our navies
    try:
        for z in range(1, 3):
            with open(sys.argv[z], "r") as file:
                i = 0
                for x in file:
                    line = x.strip("\n")
                    listem = line.split(";")
                    counter = 0
                    for y in listem:
                        if y == "":
                            counter += 1
                        else:
                            if z == 1:
                                main_list_player1[i][counter] = y
                            else:
                                main_list_player2[i][counter] = y
                            counter += 1
                    i += 1
    except:
        oyun = False
        print("An error occurred while the ships were being settled. please enter a proper entry.")
        out_file.write("An error occurred while the ships were being settled. please enter a proper entry.\n")

    # a few additional functions
    def information(h, p):
        if p == 1:
            dosya = "OptionalPlayer1.txt"
            liste = main_list_player1
        elif p == 2:
            dosya = "OptionalPlayer2.txt"
            liste = main_list_player2
        if h == "C" or h == "S" or h == "D":
            for x in range(10):
                if h in liste[x]:
                    return "-"
                elif x == 9:
                    return "X"
        else:
            with open(dosya, "r") as optional_file:
                for line in optional_file:
                    right_or_down = line.split(";")[1]
                    type_of_bottle = line.split(";")[0].split(":")[0]
                    coordinate = line.split(";")[0].split(":")[1]
                    if right_or_down == "right":
                        dic[type_of_bottle] = liste[int(coordinate.split(",")[0]) - 1][
                                              int(ord(coordinate.split(",")[1]) - 65):int(
                                                  ord(coordinate.split(",")[1]) - 65) + 2]
                    if right_or_down == "down":
                        if type_of_bottle[0] == "P":
                            dic[type_of_bottle] = [
                                liste[int(coordinate.split(",")[0]) - 1][ord(coordinate.split(",")[1]) - 65],
                                liste[int(coordinate.split(",")[0])][ord(coordinate.split(",")[1]) - 65]]
                        elif type_of_bottle[0] == "B":
                            dic[type_of_bottle] = [
                                liste[int(coordinate.split(",")[0]) - 1][ord(coordinate.split(",")[1]) - 65],
                                liste[int(coordinate.split(",")[0])][ord(coordinate.split(",")[1]) - 65],
                                liste[int(coordinate.split(",")[0]) + 1][ord(coordinate.split(",")[1]) - 65],
                                liste[int(coordinate.split(",")[0]) + 2][ord(coordinate.split(",")[1]) - 65]]
            returnn = []
            for x in dic:
                if h == x[0]:
                    if h in dic.get(x):
                        returnn.append("-")
                    else:
                        returnn.insert(0, "X")
            return " ".join(returnn)


    def list_pop(k):
        if k == 1:
            moves_list1.pop(counter)
        elif k == 2:
            moves_list2.pop(counter)
        #THE CODE FOR REMOVING THE INCORRECT ELEMENT ( move ) FROM THE MOVE LIST. SO THAT OUR COUNTER, THAT IS, THE COUNTER, DOES NOT BREAK.


    # now it is time for playing
    with open(sys.argv[3], "r") as file:
        readed1 = file.read()
        readed1 = readed1.rstrip(";")
        moves_list1 = readed1.split(";")
    with open(sys.argv[4], "r") as file:
        readed2 = file.read()
        readed2 = readed2.rstrip(";")
        moves_list2 = readed2.split(";")

    counter = 0


    def move(a):
        global error_type
        global sira_kimde
        global counter
        if a == 1:
            list = moves_list1
            main_list = main_list_player2
            player_hidden_board = player_2_hidden_board
        elif a == 2:
            list = moves_list2
            main_list = main_list_player1
            player_hidden_board = player_1_hidden_board

        if 0 < len(list[counter]) < 3:  # BURADA HOCA İNDEX EROR İÇİN SADECE GİRDİNİN 3 TEN KÜÇÜK OLDUĞU DURUMLARI ÖRNEK VERDİĞİNDEN DOLAYI
            raise IndexError            # SADECE GİRDİ 3 TEN KÜÇÜK MÜ DİYRE KONTROL EDİP KÜÇÜKSE İNDEX EROR YÜKSELTİYORUM . ÇÜNKÜ EĞER BEN KENDİM INDEX EROR
                                        # YÜKSELTMEZSEM BENİM PROGRAMIM BUNA VALUE EROR YÜKSELTİYOR .
        printt(a, list[counter], player_1_hidden_board, player_2_hidden_board)
        hamle = list[counter].split(",")
        letter = hamle[1]
        number = int(hamle[0])
        # I'm checking whether the part that should be a letter can be wrong.
        if number > 10:
            error_type = 1
            raise AssertionError
        if hamle[1] not in ord_list or len(hamle) != 2 or len(hamle[1]) != 1 or ord(letter) > 90 or ord(letter) < 65:
            raise ValueError
        if 75 <= ord(letter) <= 90:
            error_type = 2
            raise AssertionError
        if main_list[number - 1][ord(letter) - 65] == "-":
            player_hidden_board[number - 1][ord(letter) - 65] = "O"
            main_list[number - 1][ord(letter) - 65] = "O"
        elif main_list[number - 1][ord(letter) - 65] == "C" or main_list[number - 1][ord(letter) - 65] == "B" or \
                main_list[number - 1][ord(letter) - 65] == "D" or main_list[number - 1][ord(letter) - 65] == "S" or \
                main_list[number - 1][ord(letter) - 65] == "P":
            player_hidden_board[number - 1][ord(letter) - 65] = "X"
            main_list[number - 1][ord(letter) - 65] = "X"
        else:  # that leaves the X or O statements, so it's trying to do the same move a second time
            error_type = 3
            raise AssertionError
        if a == 1:           # the reason for this code is : if there is a problem with the second player's move, the program will remove that distressed element from the list
            sira_kimde = 2   # and continue the game from the first player but the program should continue the game from the second player, that is, the player from whom
        elif a == 2:         # error actually came out. These lines of code are for us to get it.
            sira_kimde = 1


    draw_or_not = False
    sira_kimde = 1
    while oyun:
        num = 0
        error_type = 0
        try:
            if sira_kimde == 1:
                if counter > len(moves_list1):
                    print("Final Information\n\nPlayer1’s Board\t\t\tPlayer2’s Board")
                    out_file.write("Final Information\n\nPlayer1’s Board\t\t\t\tPlayer2’s Board\n")
                    printt(1, "2,E", main_list_player1, main_list_player2)
                    print("Player1 has no more moves to play! The game has been terminated")
                    out_file.write("Player1 has no more moves to play! The game has been terminated\n")
                    break
                num = 1
                move(1)
            elif sira_kimde == 2:
                if counter > len(moves_list2):
                    print("Final Information\n\nPlayer1's Board\t\t\tPlayer2's Board")
                    out_file.write("Final Information\n\nPlayer1's Board\t\t\t\tPlayer2's Board\n")
                    printt(1, "2,E", main_list_player1, main_list_player2)
                    print("Player2 has no more moves to play! The game has been terminated")
                    out_file.write("Player2 has no more moves to play! The game has been terminated\n")
                    break
                num = 2
                move(2)
                roundd += 1  # when the second player plays, the counter and round will increase.
                counter += 1
        except IndexError:
            if num == 1:
                move_list=moves_list1
                player="Player1"
            elif num==2:
                move_list=moves_list2
                player="Player2"
            if counter == len(move_list):                                                          # here, if the game is not over and the players have no moves left to play,
                print(f"Final Information\n\nPlayer1's Board\t\t\tPlayer2's Board")                  # we also end the game by specifying which player has no moves left
                out_file.write("Final Information\n\nPlayer1's Board\t\t\t\tPlayer2's Board\n")
                printt(1, "2,E", main_list_player1, main_list_player2)
                print(f"{player} has no more moves to play! The game has been terminated")
                out_file.write(f"{player} has no more moves to play! The game has been terminated\n")
                break
            else:
                list_pop(num)
                print(f"IndexError: for player{num}, the inputs of your move are missing !")
                out_file.write(f"IndexError: for player{num}, the inputs of your move are missing !\n")

        except ValueError:
            print(f"ValueError: for player{num} : the inputs of the move you entered are not correct !")
            out_file.write(f"ValueError: for player{num} : the inputs of the move you entered are not correct !\n")
            list_pop(num)
        except AssertionError:
            if error_type == 3:
                print(f"AssertionError: for player{num} : you have entered the same move again !")
                out_file.write(f"AssertionError: for player{num} : you have entered the same move again !\n")
            elif error_type == 2 or error_type == 1:
                print(f"AssertionError: for player{num} : Invalid Operation.")
                out_file.write(f"AssertionError: for player{num} : Invalid Operation.\n")
            else:
                print(" kaBOOM: run for your life!")
                out_file.write(" kaBOOM: run for your life!\n")
            list_pop(num)
        except:
            print("kaBOOM: run for your life!")
            out_file.write("kaBOOM: run for your life!\n")

    # finish the game
        if sira_kimde == 1:  # yani ikinci oyuncu hamlesinin yapmış ve round tamamlanmışsa.

            set1 = set()
            set2 = set()
            for x in range(10):
                for y in main_list_player1[x]:
                    set1.add(y)
            if "C" in set1 or "B" in set1 or "D" in set1 or "S" in set1 or "P" in set1:
                player1_station = True
            else:
                player1_station = False
            for x in range(10):
                for y in main_list_player2[x]:
                    set2.add(y)
            if "C" in set2 or "B" in set2 or "D" in set2 or "S" in set2 or "P" in set2:
                player2_station = True
            else:
                player2_station = False

            if player2_station == False and player1_station == True:
                print("Final Information\n\nPlayer1's Board\t\t\tPlayer2's Board")
                out_file.write("Final Information\n\nPlayer1's Board\t\t\t\tPlayer2's Board\n")
                printt(1, "5,E", main_list_player1, main_list_player2)
                print("PLayer1 Wins!")
                out_file.write("PLayer1 Wins!\n")
                break
            elif player2_station == True and player1_station == False:
                print("Final Information\n\nPlayer1's Board\t\t\tPlayer2's Board")
                out_file.write("Final Information\n\nPlayer1's Board\t\t\t\tPlayer2's Board\n")
                printt(1, "5,E", main_list_player1, main_list_player2)
                print("Player2 Wins!")
                out_file.write("Player2 Wins!\n")
                break
            elif player2_station == True and player1_station == True:
                continue
            else:
                draw_or_not = True
                print("Final Information\n\nPlayer1's Board\t\t\tPlayer2's Board")
                out_file.write("Final Information\n\nPlayer1's Board\t\t\t\tPlayer2's Board\n")
                printt(1, "5,E", main_list_player1, main_list_player2)
                print("\nIt is a Draw!")
                out_file.write("\nIt is a Draw!\n")
                break
out_file.close()







