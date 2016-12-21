cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

#content_file <-  "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/all_aa_content.csv"
#content_file <-  "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/all_naa_content.csv"
content_file <-  "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/ForReproc/FullQAndAContent.csv"
content_data <- read.csv(content_file)


#topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq2/with_title_aa_corpus_10_topics/_TopicProb.csv"
#topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq2/with_title_naa_corpus_30_topics/_TopicProb.csv"
topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq1/you_are_never_done/_TopicProb.csv"
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
len_dic_topic   <-  length(dic_topics)        ## get the count of all questions in the corpus 
fav_count_vector    <-  content_data$FavoriteCount   ## get favorite count from content file 
fav_count_vector    <-  as.numeric(fav_count_vector)    ## convert to number 
print("------------Summary of favorite------------------")
print(summary(fav_count_vector))
for(top_inex in 1:len_top_names+1)
{
  ### temp score vector 
  temp_fav_count_vector <- vector()
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
      favCountOfQues <- fav_count_vector[counter_]
      #print(favCountOfQues)
      #print("===============")
      temp_fav_count_vector <- c( temp_fav_count_vector,  favCountOfQues)
    }
  }
  
  print("***Total questions in this topic***")
  print(q_count_topic)
  print("***Favorites for questions***")
  temp_fav_count_vector <- temp_fav_count_vector[temp_fav_count_vector != ""]
  #temp_fav_count_vector <- temp_fav_count_vector[!is.na(temp_fav_count_vector)] 
  temp_fav_count_vector[is.na(temp_fav_count_vector)] <- 0
  sumfavcnt_for_topic <- sum(temp_fav_count_vector)
  print(sumfavcnt_for_topic)  
  print("===Favorite per question===")
  fav_per_q     <- (sumfavcnt_for_topic / q_count_topic ) 
  print(fav_per_q)
  #print("===Median Of All  Favorite counts ===")
  median_fav_for_topic <- median(temp_fav_count_vector)  
  #print(median_fav_for_topic)
  #print("===Median Scores per question===")  
  median_fav_per_topic     <- (median_fav_for_topic / q_count_topic ) 
  #print(median_fav_per_topic)  
  mean_fav_for_topic <- mean(temp_fav_count_vector)
  #print("===Mean Of All Scores===")
  #print(mean_fav_for_topic)
  mean_fav_per_q     <- (mean_fav_for_topic / q_count_topic ) 
  print("===Summary of favorite for question===")
  print(summary(temp_fav_count_vector))    
  print("#########################")  

}

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))