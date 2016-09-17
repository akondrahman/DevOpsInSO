cat("\014") 
options(max.print=1000000)
library(lda)
library(tm)
library(LDAvis)
library(SnowballC)
library(topicmodels)
library(Rmpfr)
t1 <- Sys.time()
stop_words <- stopwords("SMART")
#stop_words <- c("the", "and", "you", "that", "for", "your", "are", "have", "with", "this")

file_to_read ="/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/all_aa_contents.csv"
corp2save <-    "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/aa.final.string.as.corpus.csv"
all_posts_data <- read.csv(file_to_read)
body_of_posts_data = all_posts_data$Body  

all_text_from_posts <- body_of_posts_data
all_text_from_posts <- iconv(all_text_from_posts, "ASCII", "UTF-8", sub="")

# pre-processing:
all_text_from_posts <- gsub("'", "", all_text_from_posts)  # remove apostrophes
all_text_from_posts <- gsub("[[:punct:]]", " ", all_text_from_posts)  # replace punctuation with space
all_text_from_posts <- gsub("[[:cntrl:]]", " ", all_text_from_posts)  # replace control characters with space
all_text_from_posts <- gsub("^[[:space:]]+", "", all_text_from_posts) # remove whitespace at beginning of documents
all_text_from_posts <- gsub("[[:space:]]+$", "", all_text_from_posts) # remove whitespace at end of documents
all_text_from_posts <- tolower(all_text_from_posts)  # force to lowercase
all_text_from_posts <- gsub("\\b\\w{1,2}\\b", "", all_text_from_posts)

# tokenize on space and output as a list:
string_list <- strsplit(all_text_from_posts, "[[:space:]]+")
string_list <- wordStem(string_list, language="porter")

### Code to filter out zero length strings and numerals 

checkIfInteger <- function(param)
{
  output <- as.integer(param)
  return(output) 
}
len_string_list <- length(string_list)
formatted_string_list <- vector(mode="numeric", length=len_string_list)
for(ind_ in 1:len_string_list)
{
  #print("***")
  str_=""
  elem <- string_list[ind_]
  splitted_list <- strsplit(elem, ",")
  all_splitted_Str <- splitted_list[[1]]
  for(sec_ind in 1:length(all_splitted_Str))
  {
    indi_str <- all_splitted_Str[sec_ind]
    #print(indi_str)
    core_str= unlist(strsplit(indi_str, split='\"', fixed=TRUE))[2]
    #print(core_str)
    numeric_status <- checkIfInteger(core_str) 
    #print(numeric_status)
    # & (numeric_status==NA) & (core_str!="pre") & (core_str!="code")
    if( (length(core_str)>0) & (!identical(core_str, "pre")) & (!identical(core_str, "code")) )
    {
      if(is.na(numeric_status))
      {
        #print(core_str)
        str_ <- paste(str_, core_str)
      }
    }
  }
  formatted_string_list[ind_] <- str_
  #print(str_)
  str_ = ""
}
print("After formatting ... length should be same as before ")
print(length(formatted_string_list))
write.table(formatted_string_list, file = corp2save, append = FALSE, sep = ",",
            eol = "\n", na = "NA", dec = ".", row.names = TRUE,
            col.names = TRUE)



t2 <- Sys.time()
print(t2 - t1)  # 
rm(list = setdiff(ls(), lsf.str()))