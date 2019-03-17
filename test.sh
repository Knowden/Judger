main="$(cat Main.txt)"
javac "${main}.java"

count=0
while true
do
    echo "Perform ${count} test..."
    python Builder.py > example.txt
    expr=$(cat example.txt)

    java ${main} "$expr"> temp.txt 
    ans=$(cat temp.txt) 

    python Transformer.py "$expr" > temp.txt
    input1=$(cat temp.txt)
    python Transformer.py "$ans" > temp.txt
    input2=$(cat temp.txt)

    sed -i '6, 7d' Calculater.py
    sed -i "5a ori=${input1}" Calculater.py
    sed -i "5a mine=${input2}" Calculater.py

    python Calculater.py > temp.txt

    result=$(cat temp.txt)

    if [ "$result"x != "True"x ];then
        echo "WRONG ANSWER!"
        cat example.txt >> wrong_list.txt
    else
        echo "ACCEPTED!"
    fi

    let count=count+1
done
