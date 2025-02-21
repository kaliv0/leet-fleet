#!/usr/bin/env bash

### test if strings are palindromes ###

function validate_strings(){
    local str1=$1
    local str2=$2
    local len1=${#str1}
    local len2=${#str2}

    if [[ $len1 -ne $len2 ]]; then
        echo "'$str1 <=> $str2' are not palindromes -> different lengths"
        return
    fi

    _validate $str1 $str2 $len1

    if [[ $? -ne 0 ]]; then
        echo "'$str1 <=> $str2' are not palindromes"
    else
        echo "'$str1 <=> $str2' are palindromes"
    fi
}

function _validate(){
    local str1=$1
    local str2=$2
    local len=$3

    declare -A counter

    local char1
    local char2
    for ((i=0; i<$len; i++)); do
        char1=${str1:$i:1}
        if [[ ${counter[$char1]} ]]; then
            ((counter[$char1]++))
        else
            counter[$char1]=1
        fi

        char2=${str2:$i:1}
        if [[ ${counter[$char2]} ]]; then
            ((counter[$char2]--))
        else
            counter[$char2]=-1
        fi
    done

    for key in ${!counter[@]}; do
        if [[ ${counter[$key]} -ne 0 ]]; then
            return -1
        fi  
    done
    # return 0
}

##################################

declare -A strings=(
    ["a"]="abbaacbcad dccbbbaaaa"
    ["b"]="abc xyz"
    ["c"]="abcd xyz"
)

for str in ${!strings[@]}; do
    validate_strings ${strings[$str]}
done

printf "\n######### alternative version #########\n\n"

pair1=("abbaa cbcad" "dccbb baaaa")
pair2=("abc" "xyz")
pair3=("abcd" "xyz")

strings_matrix=("pair1" "pair2" "pair3")

for pair in ${strings_matrix[@]}; do
    declare -n str_arr=$pair
    validate_strings "${str_arr[@]}"
done
