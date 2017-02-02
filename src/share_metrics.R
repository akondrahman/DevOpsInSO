cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

#topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq2/you_are_never_done/_TopicProb.csv"
topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq3/you_are_never_done/_TopicProb.csv"
#topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq1/you_are_never_done/_TopicProb.csv"
topic_prob_data <- read.csv(topic_prob_file)
total_q_count <- 59013

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
#print(dic_topics)
len_dic_topic <- length(dic_topics)
for(top_inex in 1:len_top_names+1)
{
  print("#########################")
  print(top_inex-1)
  print("---------------")

  qcount_for_topic <- 0 
  for(doc_index in 2:len_dic_topic)
  {
    tmp_ <-  dic_topics[[doc_index]][top_inex]
    if(tmp_==1)
    {
      #print("*****")
      #print("The question is:")
      #print(doc_index)
      qcount_for_topic <- qcount_for_topic + 1

    }
  }

  print("***Question Count***")
  print(qcount_for_topic)
  print("***Total Questions***")
  print(total_q_count)
  print("***Share of Questions***")
  share <- (qcount_for_topic / total_q_count ) * 100
  print(share)
  print("#########################")
}

t2 <- Sys.time()
print(t2 - t1)  # 
rm(list = setdiff(ls(), lsf.str()))