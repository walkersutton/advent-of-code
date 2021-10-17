package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	f, err := os.Open("data.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	var ids []string
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		ids = append(ids, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	var off_index int
	var bad bool
	for ii := 0; ii < len(ids) - 1; ii++ {
		id_1 := ids[ii]
		for jj := ii + 1; jj < len(ids); jj++ {
			off_index = -1
			bad = false
			id_2 := ids[jj]
			for i := range id_2 {
				if id_2[i] != id_1[i] {
					if off_index == -1 {
						off_index = i
					} else {
						bad = true
					}
				}
			}
			if !bad {
				var sb strings.Builder
				for i, c := range id_1 {
					if i != off_index {
						sb.WriteString(string(c))
					}
				}
				fmt.Println(sb.String())
			}
		}
	}
}
