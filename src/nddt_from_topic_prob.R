cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()
topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/all.corpus/30.TopicProb.csv"
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
for(doc_ind in 2:len_doc_names)
{
  
  topics_for_this_doc <- vector(mode="numeric", length=len_top_names+1)
  dom_topic_for_this_doc <- rep(0, len_top_names+1)
  for(topic_ind in 1:len_top_names+1)
  {
    topic_prob_for_doc <- topic_prob_data[doc_ind, topic_ind]
    topics_for_this_doc[topic_ind] <- topic_prob_for_doc
  }
  #topics_for_this_doc <- topics_for_this_doc[!topics_for_this_doc %in% 0.00000000]
  max_topic_prob <-  max(topics_for_this_doc)
  #print(max_topic_prob)
  index_with_max_prob <- which(topics_for_this_doc == max_topic_prob)
  #print("-----")
  #print(index_with_max_prob)
  dom_topic_for_this_doc[index_with_max_prob] <- 1
  #print(dom_topic_for_this_doc)
  dic_topics[[doc_ind]] <- dom_topic_for_this_doc
  #print("-----")  
}
#print(dic_topics)
nddt.topics <- as.matrix(dic_topics)
write.csv(nddt.topics,file=paste("nddt.topics.csv"))

len_dic_topic <- length(dic_topics)
for(top_inex in 1:len_top_names+1)
{
  nddt_for_this_topic <- vector(mode="numeric", length=len_dic_topic)
  for(doc_index in 2:len_dic_topic)
  {
    tmp_ <-  dic_topics[[doc_index]][top_inex]
    #print(tmp_)
    nddt_for_this_topic[doc_index] <-  tmp_
  }
  print("*****")
  print(top_inex)
  print("*****")
  print(sum(nddt_for_this_topic))
}


t2 <- Sys.time()
print(t2 - t1)  # 
rm(list = setdiff(ls(), lsf.str()))