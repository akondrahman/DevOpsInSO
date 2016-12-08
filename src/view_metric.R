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
len_dic_topic <- length(dic_topics)        ## get the count of all questions in the corpus 
viewvector    <-  content_data$ViewCount   ## get view counts from content file 
viewvector    <- as.numeric(viewvector)    ## convert to number 
print("------------Summary of view count------------------")
print(summary(viewvector))
for(top_inex in 1:len_top_names+1)
{
  ### temp view count vector 
  temp_view_count_vector <- vector()
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
      viewForQues <- viewvector[counter_]
      #print(viewForQues)
      #print("===============")
      temp_view_count_vector <- c( temp_view_count_vector,  viewForQues)
    }
  }
  
  print("***Total questions in this topic***")
  print(q_count_topic)
  print("***Views for questions***")
  temp_view_count_vector <- temp_view_count_vector[temp_view_count_vector != ""]
  temp_view_count_vector <- temp_view_count_vector[!is.na(temp_view_count_vector)] 
  view_for_topic <- sum(temp_view_count_vector)
  print(view_for_topic)  
  print("===Views per question===")
  view_per_q     <- (view_for_topic / q_count_topic ) 
  print(view_per_q)
  median_view_for_topic <- median(temp_view_count_vector)  
  #print("===Median Views per question===")  
  median_view_per_q     <- (median_view_for_topic / q_count_topic ) 
  #print(median_view_per_q)  
  mean_view_for_topic <- mean(temp_view_count_vector)
  mean_view_per_q     <- (mean_view_for_topic / q_count_topic ) 
  print("===Summary of views for question===")
  print(summary(temp_view_count_vector))    
  print("#########################")
}
t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))