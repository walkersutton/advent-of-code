package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
	"strconv"
)

func main() {
	f, err := os.Open("data.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)
	grid := make(map[int]map[int]int)

	claims := map[int]struct{}{}

	for scanner.Scan() {
		parts := strings.Fields(scanner.Text())
		id, err := strconv.Atoi(parts[0][1:])
		claims[id] = struct{}{}
		dimensions := strings.Split(parts[3], "x")
		width, err := strconv.Atoi(dimensions[0])
		height, err := strconv.Atoi(dimensions[1])
		topleft := strings.Split(strings.Split(parts[2], ":")[0], ",")
		x, err := strconv.Atoi(topleft[0])
		y, err := strconv.Atoi(topleft[1])
		for row := y; row < y + height; row++ {
			for col := x; col < x + width; col++ {
				if grid[row] == nil {
					grid[row] = make(map[int]int)
				}
				if (grid[row][col] == 0) {
					grid[row][col] = id
				} else if (grid[row][col] > 0) {
					delete(claims, grid[row][col])
					delete(claims, id)
				}
			}
		}
		if err != nil {
			log.Fatal(err)
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	for key, _ := range claims {
		fmt.Println(key)
	}
}
