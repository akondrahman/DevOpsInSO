cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

#content_file <-  "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/garbage/all_aa_contents.csv"
#content_file <-  "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/garbage/all_naa_contents.csv"
content_file <-  "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/all_needed_content.csv"
content_data <- read.csv(content_file)

#topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq2/with_title_aa_corpus_10_topics/_TopicProb.csv"
#topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq2/with_title_naa_corpus_30_topics/_TopicProb.csv"
topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq1/with_title_all_corpus_20_topics/_TopicProb.csv"
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
len_dic_topic           <-  length(dic_topics)        ## get the count of all questions in the corpus 
comment_count_vector    <-  content_data$CommentCount   ## get answer count from content file 
comment_count_vector    <-  as.numeric(comment_count_vector)    ## convert to number 
print("------------Summary of comment count------------------")
print(summary(comment_count_vector))

for(top_inex in 1:len_top_names+1)
{
  ### temp score vector 
  temp_comm_count_vector <- vector()
  ### counter_ for all questions 
  counter_ <- 0 
  ### counter for questions for this topic 
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
      q_count_topic <- q_count_topic + 1
      commCountOfQues <- comment_count_vector[counter_]
      #print(commCountOfQues)
      #print("===============")
      temp_comm_count_vector <- c( temp_comm_count_vector,  commCountOfQues)
    }
  }
  
  print("***Total questions in this topic***")
  print(q_count_topic)
  #print((temp_comm_count_vector))
  print("***Comment count for all questions***")
  temp_comm_count_vector <- temp_comm_count_vector[temp_comm_count_vector != ""]
  temp_comm_count_vector <- temp_comm_count_vector[!is.na(temp_comm_count_vector)] 
  sum_comm_for_topic <- sum(temp_comm_count_vector)
  print(sum_comm_for_topic)  
  print("===Comment count per question===")
  commCount_per_q     <- (sum_comm_for_topic / q_count_topic ) 
  print(commCount_per_q)
  #print("===Median Of All Comment counts ===")
  median_comm_for_topic <- median(temp_comm_count_vector)  
  #print(median_comm_for_topic)
  #print("===Median Comments per question===")  
  median_comm_per_question     <- (median_comm_for_topic / q_count_topic ) 
  #print(median_comm_per_question)  
  mean_comm_for_topic <- mean(temp_comm_count_vector)
  #print("===Mean Of Answers===")
  #print(mean_comm_for_topic)
  mean_comm_per_q     <- (mean_comm_for_topic / q_count_topic ) 
  print("===Summary of comment count per question===")
  print(summary(temp_comm_count_vector))    
  print("#########################")  
  
}

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))