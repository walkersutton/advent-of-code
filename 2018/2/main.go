package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	f, err := os.Open("data.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)

	var twos int = 0
	var threes int = 0

	for scanner.Scan() {
		set := make(map[string]int)
		hit_two := false
		hit_three := false

		line := scanner.Text()
		for _, c := range line {
			set[string(c)] += 1
		}
		for _, v := range set {
			if v == 2 && !hit_two  {
				twos += 1
				hit_two = true
			} else if v == 3 && !hit_three {
				threes += 1
				hit_three = true
			}
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(twos * threes)
}
