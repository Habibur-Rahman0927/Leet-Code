class Solution(object):
    def imageSmoother(self, img):
        output = []
        for r in range(0, len(img)):
            tmp = []
            for c in range(0, len(img[r])):
                count, avg = 0, 0
                for i in range(max(0, r - 1), min(len(img), r + 2)):
                    for j in range(max(0, c - 1), min(len(img[r]), c + 2)):
                        count += 1
                        avg += img[i][j]
                tmp.append(avg//count)
            output.append(tmp)
        return output

solution = Solution()
print(solution.imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))