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

	scanner := bufio.NewScanner(f)

	var total int = 0

	for scanner.Scan() {
		line := scanner.Text()
		sign := line[0:1]
		value, err := strconv.Atoi(line[1:])

		if err != nil {
			log.Fatal(err)
		} else if sign == "+" {
			total += value
		} else {
			total -= value
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(total)
}
