cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

content_file <-  "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/all_needed_content.csv"
content_data <- read.csv(content_file)


topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq1/with_title_all_corpus_20_topics/_TopicProb.csv"
topic_prob_data <- read.csv(topic_prob_file)

topic_names <- colnames(topic_prob_data, do.NULL = TRUE, prefix = "col")
doc_names <- rownames(topic_prob_data, do.NULL = TRUE, prefix = "row")

topic_names <- topic_names[!topic_names %in% "X"]
#print(topic_names)
#print(doc_names)
len_doc_names <- length(doc_names)
len_top_names <- length(topic_names)
dic_topics <- vector(mode="list", length=len_doc_names)
names(dic_topics) <- doc_names
###threshold 
topic_prob_cutoff <- 0.10

for(doc_ind in 2:len_doc_names)
{
  
  topics_for_this_doc <- vector(mode="numeric", length=len_top_names+1)
  dom_topic_for_this_doc <- rep(0, len_top_names+1)
  for(topic_ind in 1:len_top_names+1)
  {
    topic_prob_for_doc <- topic_prob_data[doc_ind, topic_ind]
    topics_for_this_doc[topic_ind] <- topic_prob_for_doc
  }
  #max_topic_prob <-  max(topics_for_this_doc)
  #print(max_topic_prob)
  index_with_max_prob <- which(topics_for_this_doc >= topic_prob_cutoff)
  #print("-----")
  #print(index_with_max_prob)
  dom_topic_for_this_doc[index_with_max_prob] <- 1
  #print(dom_topic_for_this_doc)
  dic_topics[[doc_ind]] <- dom_topic_for_this_doc
  #print("-----")  
}
len_dic_topic       <-  length(dic_topics)        ## get the count of all questions in the corpus 
ans_count_vector    <-  content_data$AnswerCount   ## get answer count from content file 
ans_count_vector    <-  as.numeric(ans_count_vector)    ## convert to number 
print("------------Summary of answer count------------------")
print(summary(ans_count_vector))


t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))