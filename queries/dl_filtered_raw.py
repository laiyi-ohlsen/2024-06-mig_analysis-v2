query=f'''
SELECT
  server.Site as site,
  date, 
  a.MeanThroughputMbps as download
FROM `measurement-lab.ndt_intermediate.extended_ndt7_downloads`
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
AND (filter.IsComplete -- Not missing any important fields
      AND filter.IsProduction -- not a test server
      AND NOT filter.IsError -- Server reported an error
      AND NOT filter.IsOAM -- operations and management traffic
      AND NOT filter.IsPlatformAnomaly -- overload, bad version, etc
      AND NOT filter.IsSmall -- less than 8kB data
      AND (NOT filter.IsShort OR filter.IsEarlyExit) -- insufficient duration or early exit.
      AND NOT filter.IsLong -- excessive duraton
      -- TODO(https://github.com/m-lab/k8s-support/issues/668) deprecate? _IsRFC1918
      AND NOT filter._IsRFC1918)
      '''