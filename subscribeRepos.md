# com.atproto.sync.subscribeRepos
## 

Subscribe to repo updates

**Type**: subscription

### Parameters

**cursor**: *integer*
The last known event to backfill from.

### Errors

**FutureCursor**: 

**ConsumerTooSlow**: 

## commit

**Type**: object

### Properties

**seq**: *integer*


**rebase**: *boolean*


**tooBig**: *boolean*


**repo**: *string*


**commit**: *cid-link*


**prev**: *cid-link*


**rev**: *string*
The rev of the emitted commit

**since**: *string*
The rev of the last emitted commit from this repo

**blocks**: *bytes*
CAR file containing relevant blocks

**ops**: *array*


**blobs**: *array*


**time**: *string*


## handle

**Type**: object

### Properties

**seq**: *integer*


**did**: *string*


**handle**: *string*


**time**: *string*


## migrate

**Type**: object

### Properties

**seq**: *integer*


**did**: *string*


**migrateTo**: *string*


**time**: *string*


## tombstone

**Type**: object

### Properties

**seq**: *integer*


**did**: *string*


**time**: *string*


## info

**Type**: object

### Properties

**name**: *string*


**message**: *string*


## repoOp

A repo operation, ie a write of a single record. For creates and updates, cid is the record's CID as of this operation. For deletes, it's null.

**Type**: object

### Properties

**action**: *string*


**path**: *string*


**cid**: *cid-link*



