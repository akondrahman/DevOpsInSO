USE DevOpsInSO; 
-- SELECT COUNT(*) FROM no_txt_all_au_;
-- SELECT COUNT(*) FROM no_txt_all_sf_;
-- SELECT COUNT(*) FROM no_txt_all_su_;
-- SELECT COUNT(*) FROM no_txt_all_unix_;
-- SELECT COUNT(*) FROM no_txt_all_so_;
-- Number of questions : 92513 
-- SELECT COUNT(Id) FROM no_txt_all_so_ WHERE PostTypeId=1; 
-- Number fo questions with accepted answers: 40881 
-- SELECT AcceptedAnswerId FROM no_txt_all_so_ WHERE 
--    Id IN ( SELECT Id FROM no_txt_all_so_ ) AND AcceptedAnswerId > 0
--    LIMIT 0, 50000;
-- For sanity check 
-- SELECT * FROM no_txt_all_so_ WHERE Id=24361908;
--  SELECT * FROM no_txt_all_so_ WHERE Id=22129969;
-- Date and time when accepted answers are created 

-- Date and time when questions are created 
-- SELECT CreationDate FROM no_txt_all_so_ WHERE 
--   Id IN ( SELECT Id FROM no_txt_all_so_ ) ;



-- Sep 14, 2016 --
-- SELECT AcceptedAnswerId FROM no_txt_all_unix_ WHERE 
--    Id IN ( SELECT Id FROM no_txt_all_unix_ ) 
--    AND AcceptedAnswerId > 0 LIMIT 0, 50000;


-- Sep 15, 2016 --
-- SELECT COUNT(AnswerCount) FROM no_txt_all_so_ WHERE 
--    Id IN ( SELECT Id FROM no_txt_all_so_ ) 
--    AND AnswerCount <= 0 LIMIT 0, 50000;

-- SELECT Id AS AA_ID FROM no_txt_all_au_ WHERE 
--    AcceptedAnswerId > 0 LIMIT 0, 100000;


-- Sep 16, 2016 ----
-- SELECT AcceptedAnswerId, CreationDate, Score, ViewCount, AnswerCount, CommentCount, FavoriteCount 
-- FROM no_txt_all_au_ WHERE `AcceptedAnswerId` > 0;
-- SELECT COUNT(*) 
-- FROM no_txt_all_au_ ;

-- Sep 22, 2016 ----
-- SELECT AcceptedAnswerId, CreationDate, Score, ViewCount, AnswerCount, CommentCount, FavoriteCount 
-- FROM no_txt_all_so_ WHERE `AcceptedAnswerId` > 0 LIMIT 0, 50000;
-- SELECT COUNT(DISTINCT(AcceptedAnswerId)) FROM no_txt_all_so_ WHERE `AcceptedAnswerId` > 0;