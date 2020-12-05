package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	f, err := os.Open("data.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	values := make([]int, 0)

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()
		sign := line[0:1]
		value, err := strconv.Atoi(line[1:])

		if err != nil {
			log.Fatal(err)
		} else if sign == "+" {
			values = append(values, value)
		} else {
			values = append(values, value * -1)
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	var total int = 0
	s := map[int]bool{total: true}

Jump:

	for _, value := range values {
		total += value
		if !s[total] {
			s[total] = true
		} else {
			fmt.Println(total)
			return
		}
	}
	goto Jump
}
