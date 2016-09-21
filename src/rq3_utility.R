cat("\014") 
options(max.print=1000000)
corpusFile <- 
t1 <- Sys.time()
all_needed_file <-  "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/all_needed_content.csv"
rq3_data_file_body  <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/rq3_data_body.csv"
rq3_data_file_title  <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/rq3_data_title.csv"
all_posts_data <- read.csv(all_needed_file)

## generate random indices os 95% stats. confidence and 5% CI 
# set the params
### https://www.surveymonkey.com/mp/sample-size-calculator/ 
### This sample size calculator uses a normal distribution (50%) to calculate your optimum sample size.
cnt_elems_to_pick <- 383 ### determined by http://www.surveysystem.com/sscalc.htm  
len_ <- nrow(all_posts_data)
print("Count of entries in corpus")
print(len_)
### get the random indices
indicesTochoose <- sample(1:len_, cnt_elems_to_pick, replace=FALSE)
#print(indicesTochoose)
selected_matrix <- all_posts_data[indicesTochoose, ]
##print(head(selected_matrix))
# get body 
mat2dump_Body <- selected_matrix$Body
write.table(mat2dump_Body,file=rq3_data_file_body, sep=",") 
# get title 
mat2dump_Title <- selected_matrix$Title
write.table(mat2dump_Title,file=rq3_data_file_title, sep=",") 
t2 <- Sys.time()
print(t2 - t1)  # 
rm(list = setdiff(ls(), lsf.str()))