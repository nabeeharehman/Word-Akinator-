'''INSERT FUNCTION
    PARAMETERS: TERNARY TREE
                 WORD TO BE INSERTED
    DEFINITION: A RECURSIVE APPROACH TO INSERTING A WORD INTO THE TERNARY TREE'''
def insert(tree:dict, word:str):
    if not word:
        return

    char = word[0]
    
    if 'root' not in tree:
        tree['root']=char
        if len(word)==1:
            tree['end_of_word']=1
            tree['mid'],tree['right'],tree['left']={},{},{}
            return
        else:
            tree['end_of_word'] = 0
            tree['mid'],tree['right'],tree['left']={},{},{}
            insert(tree['mid'],word[1:])
        

    elif tree['root']==None:
        tree['root']=char
        insert(tree['mid'],word[1:])
        
        
    

    

    else:
        if char<tree['root']:
            insert(tree['left'],word)
        elif char>tree['root']:
            insert(tree['right'],word)
        
        else:
        
            if len(word)==1:
                tree['end_of_word']=1
            else:
                insert(tree['mid'],word[1:])

'''TRAVERSE FUNCTION
    PARAMETERS: TERNARY TREE
                
    DEFINITION: A RECURSIVE APPROACH TO OUTPUT ALL THE WORDS IN THE TERNARY TREE'''
def traverse(tree:dict, result:list, prefix=''):
    if 'root' not in tree:
        return

    if tree['end_of_word'] == 1:
        result.append(prefix + tree['root'])

    traverse(tree['left'], result, prefix)
    traverse(tree['mid'], result, prefix + tree['root'])
    traverse(tree['right'], result, prefix)


'''EXIST FUNCTION
    PARAMETERS: TERNARY TREE
                WORD TO CHECK THE EXISTENCE 
                
    DEFINITION: A RECURSIVE APPROACH TO CHECK THE EXISTENCE OF A WORD IN THE TERNARY TREE'''
def exist(tree: dict, word: str) -> bool:
    if not word:
        return False

    char = word[0]

    if 'root' not in tree:
        return False

    if tree['root'] == char:
        if len(word) == 1:
            return tree.get('end_of_word', 0) == 1
        return exist(tree.get('mid', {}), word[1:])
    elif char < tree['root']:
        return exist(tree.get('left', {}), word)
    else:
        return exist(tree.get('right', {}), word)


'''DELETE FUNCTION
    PARAMETERS: TERNARY TREE
                WORD TO BE DELETED
    DEFINITION: A RECURSIVE APPROACH TO DELETE THE WORD FROM THE TERNARY TREE'''
def delete(tree: dict, word: str):
    if not exist(tree, word):
        print("The word '{}' does not exist in the tree.".format(word))
        return

    delete_helper(tree, word,0)


def delete_helper(tree: dict, word: str, index: int):
    if not tree:
        return

    char = word[index]
    if char == tree['root']:
        if index == len(word) - 1:
            if tree.get('end_of_word', 0) == 1:
                tree['end_of_word']=0
                
                if not tree.get('left') and not tree.get('mid') and not tree.get('right'):
                    del tree['root'],tree['left'],tree['right'],tree['mid']
            return
        else:
            delete_helper(tree.get('mid', {}), word, index + 1)
        
        
        if not tree.get('mid') and not tree.get('left') and not tree.get('right'):
            del tree['root'],tree['left'],tree['right'],tree['mid'],tree['end_of_word']
    elif char < tree['root']:
        delete_helper(tree.get('left', {}), word, index)
    else:
        delete_helper(tree.get('right', {}), word, index)



'''RETURN TREE FROM A NODE FUNCTION
    PARAMETERS: TERNARY TREE
                WORD AFTER WHICH THE SUBTREE IS NEEDED
    DEFINITION: A RECURSIVE APPROACH TO OUTPUT THE SUBTREE AFTER A WORD HAS BEEN FOUND'''
def return_tree(tree,word):
    if not word:
        return False

    char = word[0]

    if 'root' not in tree:
        return False

    if tree['root'] == char:
        if len(word) == 1:
            return tree['mid']
        return return_tree(tree.get('mid', {}), word[1:])
    elif char < tree['root']:
        return return_tree(tree.get('left', {}), word)
    else:
        return return_tree(tree.get('right', {}), word)
    

'''EXIST FUNCTION
    PARAMETERS: TERNARY TREE
                PREFIX OF A WORD
    DEFINITION: A RECURSIVE APPROACH TO CHECK THE EXISTENCE OF A PREFIX IN A WORD'''
def exist_prefix_in_tree(tree:dict,prefix:str) -> bool:

    if not prefix:
        return False

    char = prefix[0]

    if 'root' not in tree:
        return False

    if tree['root'] == char:
        if len(prefix) == 1:
            return True
        return return_tree(tree.get('mid', {}), prefix[1:])
    elif char < tree['root']:
        return return_tree(tree.get('left', {}), prefix)
    else:
        return return_tree(tree.get('right', {}), prefix)

'''TRAVERSE FUNCTION
    PARAMETERS: TERNARY TREE
                PREFIX OF A WORD
    DEFINITION: A RECURSIVE APPROACH TO OUTPUT ALL THE WORDS BEGINNING FROM THE PREFIX IN THE WORD'''
def autocomplete(tree: dict, prefix: str) -> list:
    if exist_prefix_in_tree(tree,prefix)==False:
        a=input('This word does not exist in the tree. Would you like to add it in the dictionary? yes/no ')
        if a=='yes':
            insert(tree,prefix)
        else:
            return False
    suggestions = []
    subtree=return_tree(tree,prefix)
    result_temp=[]
    traverse(subtree,result_temp)
    if exist(tree,prefix)==True:
        suggestions.append(prefix)
    for i in result_temp:
        suggestions.append(prefix+i)

    return suggestions

'''HIGHEST FREQUENCE FUNCTION
    PARAMETERS: LIST OF WORDS
                DICTIONARY WITH WORDS AS KEYS AND THEIR FREQUENCY AS VALUE
    DEFINITION: FUNCTION RETURNS THE WORD WITH HIGHEST FREQUENCY '''
def highest_frequency(lst:list,dic:dict):
    res=[]
    high=0
    for i in lst:
        if dic[i]>=high:
            if dic[i]==high:
                res.append(i)
            else:
                res=[i]
            high=dic[i]
    return res



        


def main(filename):
    with open(filename) as f:
        lines= f.readlines()

    
    words=[]
    for line in lines:
        line= line.strip()
        words.append(line)

    words=words[1:]
    

    tree = {'root': None, 'right': {}, 'left': {}, 'mid': {},'end_of_word':0}
    for word in words:
        insert(tree,word)

    

    freq={}
    for item in words:
        freq[item]=0

    print("******************************************************")
    print("HELLO AND WELCOME TO WORD AKINATOR. I CAN READ YOUR MIND. DON'T BELIEVE ME? GIVE IT A TRY!")
    print("HERE IS THE OPERATIONS I CAN DO")
    ch='yes'
    while ch=='yes':
        print("*********************")
        print("CHOICE 1: PLAY A GUESSING GAME WITH COMPUTER")
        print("CHOICE 2: INSERT A WORD IN YOUR DICTIONARY")
        print("CHOICE 3: DELETE A WORD FROM YOUR DICTIONARY")
        print("CHOICE 4: PRINT ALL WORDS IN YOUR DICTIONARY")
        print("CHOICE 5: CHECK THE EXISTENCE OF A WORD IN YOUR DICTIONARY")
        print("*********************")
        choice=input("ENTER YOUR CHOICE: ")
        if choice=='1':
            print("*********************")
            print("THINK OF A WORD. BUT DON'T TELL US YET!")
            prefix= input("Enter a part or prefix of the word: ")
            
            if exist_prefix_in_tree(tree,prefix)=={}:
                print('This word does not exist in the tree.')
                
                
            

            elif type(autocomplete(tree,prefix))==list:
                result=(autocomplete(tree,prefix))
                final=highest_frequency(result,freq)


                if len(final)>1:
                    print("IS YOUR GUESS IN: ")
                    print(final)
                    confirm=input("YES OR NO? ")
                    if confirm=='yes':
                        think=input("WHAT WAS YOUR WORD? ")
                        freq[think]+=1000
                    elif confirm=='no':
                        think=input("WHAT WAS YOUR WORD? ")
                        insert(tree,think)
                        freq[think]=1
                        print("WORD SUCCESSFULLY INSERTED IN DICTIONARY")

                elif len(final)==1:
                    print("YOUR GUESS IS: ")
                    print(final)
                    confirm=input("YES OR NO? ")
                    if confirm=='no':
                        think=input("WHAT WAS YOUR WORD? ")
                        insert(tree,think)
                        freq[think]=1
                        print("WORD SUCCESSFULLY INSERTED IN DICTIONARY")
            

        elif choice=='2':
            print("*********************")
            inserts=input("ENTER THE WORD YOU WISH TO INSERT ")
            insert(tree,inserts)
            print("SUCCESSFULLY INSERTED")
        elif choice=='3':
            print("*********************")
            deletes= input("ENTER THE WORD YOU WISH TO DELETE ")
            delete(tree,deletes)
            print("SUCCESSFULLY DELETED")
        elif choice=='4':
            print("*********************")
            res=[]
            traverse(tree,res)
            print("THE WORDS PRESENT IN THE TREE ARE:")
            for j in res:
                print(j)
        elif choice=='5':
            print("*********************")
            exists=input("ENTER THE WORD YOU WISH TO CHECK THE EXISTENCE OF ")
            if exist(tree,exists)==True:
                print("{} EXISTS IN THE DICTIONARY".format(exists))
            else:
                print("{} DOES NOT EXISTS IN THE DICTIONARY".format(exists))
                






                
        ch=input("DO YOU WANT TO CONTINUE? yes/no ")

            

                        


            
        




    
    

    



    

main('4000-most-common-english-words-csv.csv')



# 'TEST CASES'
# tree = {'root': None, 'right': {}, 'left': {}, 'mid': {},'end_of_word':0}


# lst=['hello','hell','bye','egg','egghead','eggplant','eggshell']
# for word in lst:
#     insert(tree,word)


# print(exist(tree,'hell'))  #should print True
# print()
# print(exist(tree,'hello')) #prints True
# print()
# print(autocomplete(tree,'egg')) #prints ['egg', 'egghead', 'eggplant', 'eggshell']
# print()
# res=[]
# traverse(tree,res)
# print(res)
# print()


# delete(tree,'hello')
# res=[]
# traverse(tree,res)
# print(res)
# #should print ['bye', 'egg', 'egghead', 'eggplant', 'eggshell', 'hell']



