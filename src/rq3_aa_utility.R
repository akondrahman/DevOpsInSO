cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

all_needed_file <-  "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/all_needed_content.csv"
rq3_data_file_body  <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/rq3_aa_data_body.csv"
rq3_data_file_title  <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/rq3_aa_data_title.csv"
rq3_data_file_indicies <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/rq3_aa_data_index.txt"
all_posts_data <- read.csv(all_needed_file)

all_aa_id_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/all_aa_id.csv"
all_aa_id_data <- read.csv(all_aa_id_file)
all_aa_id_ <- all_aa_id_data$AA_ID

id_in_all_content <- all_posts_data$Id
aa_matching_indecies <- match(all_aa_id_, id_in_all_content)
aa_matrix_ <- all_posts_data[aa_matching_indecies, ]


cnt_elems_to_pick <- 381 ### determined by http://www.surveysystem.com/sscalc.htm  
len_ <- nrow(aa_matrix_)
print("Count of entries in corpus")
print(len_)
### get the random indices
indicesTochoose <- sample(1:len_, cnt_elems_to_pick, replace=FALSE)
write.table(indicesTochoose,file=rq3_data_file_indicies, sep=",") 
selected_matrix <- aa_matrix_[indicesTochoose, ]
# get body 
mat2dump_Body <- selected_matrix$Body
write.table(mat2dump_Body,file=rq3_data_file_body, sep=",") 
# get title 
mat2dump_Title <- selected_matrix$Title
write.table(mat2dump_Title,file=rq3_data_file_title, sep=",") 

t2 <- Sys.time()
print(t2 - t1)  # 
rm(list = setdiff(ls(), lsf.str()))