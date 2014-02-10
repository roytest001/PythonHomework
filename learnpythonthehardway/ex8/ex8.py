#coding=utf-8 
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, True, True, False)
print formatter % (formatter, formatter, formatter, formatter)

#为啥打印输出双引号,为什么 %r 有时打印出来的是单引号,而我实际用的是双引号?
#Python 会用最有效的方式打印出字符串,而不是完全按照你写的方式来打印。这样做对于 %r 来 说是可以接受的,因为它是用作 debug 和排错,没必要非打印出多好看的格式。

print formatter % (
	"I think this is a bug.",
	"That you could type up right",
	"But it didn't sing.",
	"So I said goodnight."
	)n