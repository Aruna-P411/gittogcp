SELECT * FROM `ai-practice-388514.GECX_MO_EBCP.Participants`;

UPDATE `ai-practice-388514.GECX_MO_EBCP.Enrollment`
SET plan = 'Healthy Blue'
WHERE enrollment_id = 'ENR3'
  AND participant_id = 'MO100011'
  AND plan = 'Molina';