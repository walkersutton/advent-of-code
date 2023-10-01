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

  // [1518-11-01 00:00] Guard #10 begins shift
  // [1518-11-01 00:05] falls asleep
  // [1518-11-01 00:25] wakes up
  // [1518-11-01 00:30] falls asleep
  // [1518-11-01 00:55] wakes up
  // [1518-11-01 23:58] Guard #99 begins shift
  // [1518-11-02 00:40] falls asleep
  // [1518-11-02 00:50] wakes up
  // [1518-11-03 00:05] Guard #10 begins shift

  guards := make(map[int]int)
  var guard int = -1

	for scanner.Scan() {
    line := scanner.Text()
	  parts := strings.Fields(line)
    l := len(parts)
    action := parts[l:l+1]
    if action == "shift" {
      guard = strconv.Atoi(parts[l-2:l-1][1:])
      fmt.Println("the guard changed!") 
      fmt.Println(guard)
      guards[guard] = 0
    }
		
		// guard := strings.Split(parts[3], "]")
    // parts = parts[1:strings.StringLength(te)]
	  // fmt.Println(parts)
    //   action := strings.Split(v, "]")[1]

    //   fmt.Println(v)
	  // fmt.Println(parts)
    // fmt.Println(strings.Split(parts[1], ""))
	  // fmt.Println(strings.Split(parts[1], "]"))
	  // fmt.Println(strings.Split(parts[2], "]"))
		// width, err := strconv.Atoi(dimensions[0])
		// height, err := strconv.Atoi(dimensions[1])
		// topleft := strings.Split(strings.Split(parts[2], ":")[0], ",")
		// x, err := strconv.Atoi(topleft[0])
		// y, err := strconv.Atoi(topleft[1])
		// for row := y; row < y + height; row++ {
		// 	for col := x; col < x + width; col++ {
		// 		if grid[row] == nil {
		// 			grid[row] = make(map[int]int)
		// 		}
		// 		if (grid[row][col] != -1) {
		// 			grid[row][col] += 1
		// 			if (grid[row][col] > 1) {
		// 				count += 1
		// 				grid[row][col] = -1
		// 			}
		// 		}
		// 	}
		// }
		if err != nil {
			log.Fatal(err)
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	// fmt.Println(count)
}
