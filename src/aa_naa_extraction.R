cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

all_needed_file <-  "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/all_needed_content.csv"
all_posts_data <- read.csv(all_needed_file)

all_aa_id_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/all_aa_id.csv"
all_aa_id_data <- read.csv(all_aa_id_file)
all_aa_id_ <- all_aa_id_data$AA_ID

all_naa_id_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/all_naa_id.csv"
all_naa_id_data <- read.csv(all_naa_id_file)
all_naa_id_ <- all_naa_id_data$NAA_ID

########NAA Extraction Zone Started #######
naa_file_name <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/all_naa_content.csv"
id_in_all_content <- all_posts_data$Id
naa_matching_indecies <- match(all_naa_id_, id_in_all_content)
#print((naa_matching_indecies))
naa_matrix_body <- all_posts_data[naa_matching_indecies, ]
naa_matrix_body <- naa_matrix_body[-1, ]
naa_matrix_body <- naa_matrix_body[, -c(9, 16, 17)]
print("NAA Matrix Dumping")
print(dim(naa_matrix_body))
print(head(naa_matrix_body))
write.csv(naa_matrix_body,file=naa_file_name, row.names=FALSE, na='0') 
###naa_matrix_title <- naa_matrix_body$Title
###write.table(naa_matrix_title, file=naa_file_name, sep=",", col.names=NA)
########NAA Extraction Zone Ended #######


########AA Extraction Zone Started #######
aa_file_name <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/all_aa_content.csv"
id_in_all_content <- all_posts_data$Id
aa_matching_indecies <- match(all_aa_id_, id_in_all_content)
#print((aa_matching_indecies))
aa_matrix_body <- all_posts_data[aa_matching_indecies, ]
aa_matrix_body <- aa_matrix_body[-1, ]
aa_matrix_body <- aa_matrix_body[, -c(9, 16, 17)]
print("AA Matrix Dumping")
print(dim(aa_matrix_body))
print(head(aa_matrix_body))
write.csv(aa_matrix_body,file=aa_file_name, row.names=FALSE, na='0') 
# aa_matrix_title <- aa_matrix_body$Title
# print(aa_matrix_title)
# write.table(aa_matrix_title, file=aa_file_name, sep=",", col.names=NA)
########AA Extraction Zone Started #######
t2 <- Sys.time()
print(t2 - t1)  # 
rm(list = setdiff(ls(), lsf.str()))