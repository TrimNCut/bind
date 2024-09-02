NOTE : THIS IS JUST THE FIRST SYNTAX EXAMPLE

'''
    Language syntax:

        -- is to comment
        
        -- VARIABLES
        new a = 5;
        new b = 3;

        -- FUNCTIONS
        new func test(a, b){
            -- IF STATEMENTS
            if a > b {
                return a;
            } elif b > a{
                return b;
            } else{
                return 0;
            }
        }

        -- OUTPUTING IN TERMINAL
        write(test(a, b));

        new func test2(a, b){

            -- LOOPS
            for new i = 1, i <= 5 {
                write(i);
            }

            new condition = true;
            new counter = 1;

            while condition{
                if counter >= 5{
                    write("Done!");
                    end;
                }
                counter += 1;
            }

            counter = 1;

            do {
                if counter >= 5{
                    write("Done!");
                    end;
                }
                counter += 1;
            }while condition;

            new testList = ["a", "b", "c"];
            
            testList.map(item,index,new func printItems(){
                writef("Item at ${index} : ${item}");
                -- Output would be :
                -- Item at 0 : a
                -- Item at 1 : b
                -- Item at 2 : c
            });
        }
'''