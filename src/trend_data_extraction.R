cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

content_file <-  "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/all_aa_content.csv"
#content_file <-  "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/all_naa_contents.csv"
#content_file <-  "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/all_needed_content.csv"
content_data <- read.csv(content_file)

print("------------Head of content------------------")
print(head(content_data))

topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq2/with_title_aa_corpus_10_topics/_TopicProb.csv"
#topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq2/with_title_naa_corpus_30_topics/_TopicProb.csv"
#topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq1/with_title_all_corpus_20_topics/_TopicProb.csv"
topic_prob_data <- read.csv(topic_prob_file)

topic_names <- colnames(topic_prob_data, do.NULL = TRUE, prefix = "col")
doc_names <- rownames(topic_prob_data, do.NULL = TRUE, prefix = "row")

topic_names <- topic_names[!topic_names %in% "X"]

len_doc_names <- length(doc_names)
len_top_names <- length(topic_names)
dic_topics <- vector(mode="list", length=len_doc_names)
names(dic_topics) <- doc_names
###threshold 
topic_prob_cutoff <- 0.10

for(doc_ind in 2:len_doc_names)
{
  
  topics_for_this_doc <- vector()
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
len_dic_topic           <-  length(dic_topics)          ## get the count of all questions in the corpus 
createDate_vector       <-  content_data$CreationDate   ## get creation date from content file 
origID_vector           <-  content_data$Id             ## get ID from content file 

print("------------Summary of creation date------------------")
print(summary(createDate_vector))

###the vector that holds verything 
fullContent <- c()
### temp vector for holdind indi. stuff 
idContent   <- c()
dateContent <- c()
topIndCont  <- c()
origIDCont  <- c() 
for(top_inex in 1:len_top_names+1)
{
  ### counter for questions for this topic   
  counter_ <- 0 
  ###  for holding the contents for each topic 
  q_count_topic <- 0 
  print("#########################")
  print("Topic #")
  print(top_inex-1)
  for(doc_index in 2:len_dic_topic)
  {
    counter_ <- counter_ + 1 
    tmp_ <-  dic_topics[[doc_index]][top_inex]
    if(tmp_==1)
    {
      #q_count_topic     <- q_count_topic + 1
      createDateForQues <- as.character(createDate_vector[counter_])
      origIDForQues     <- origID_vector[counter_]
      quesID            <- doc_index - 1
      topicNumber       <- top_inex - 1
      #print(createDateForQues)
      idContent         <-c(idContent, quesID)
      dateContent       <-c(dateContent, createDateForQues)
      topIndCont        <-c(topIndCont, topicNumber)
      origIDCont        <-c(origIDCont, origIDForQues)
    }
  }

  print("#########################")
}
print("----- The final string to dump -----")
fullContent  <- data.frame(idContent, dateContent, topIndCont, origIDCont)
print(head(fullContent))

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))