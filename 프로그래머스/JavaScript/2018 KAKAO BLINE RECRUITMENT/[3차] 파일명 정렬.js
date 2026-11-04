function solution(files) {
        return files
        .map((file, index) => {
            const match = file.match(/^([^0-9]+)([0-9]{1,5})/)

            return {
                file,
                head: match[1].toLowerCase(),
                number: Number(match[2]),
                index
            }
        })
        .sort((a, b) => {
            if (a.head !== b.head) {
                return a.head.localeCompare(b.head)
            }

            if (a.number !== b.number) {
                return a.number - b.number
            }

            return a.index - b.index
        })
        .map(v => v.file)
}