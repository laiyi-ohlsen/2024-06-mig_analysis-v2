query=f'''
SELECT
  server.Site as site,
  date, 
  a.MeanThroughputMbps as download
FROM `measurement-lab.ndt.ndt7`
WHERE (DATE BETWEEN '2024-03-28' AND '2024-04-04')
AND Server.site IN (
  'chs01', 'chs02',
  'dfw09', 'dfw12',
  'lax07', 'lax10',
  'yul07', 'yul08',
  'gru05', 'gru06',
  'hel01', 'hel02'
  'waw01', 'waw02',
  'zrh01', 'zrh02', 
  'doh01', 'doh02',
  'bom03', 'bom06', 
  'cgk01', 'cgk02', 
  'icn01', 'icn02'
  )
      '''