    def _rotate_checkpoints(self, use_mtime=False) -> None:
        if self.args.save_total_limit is None or self.args.save_total_limit <= 0:
            return

        # Check if we should delete older checkpoint(s)
        checkpoints_sorted = self._sorted_checkpoints(use_mtime=use_mtime)
        if len(checkpoints_sorted) <= self.args.save_total_limit:
            return

        number_of_checkpoints_to_delete = max(0, len(checkpoints_sorted) - self.args.save_total_limit)
        checkpoints_to_be_deleted = checkpoints_sorted[:number_of_checkpoints_to_delete]
        for checkpoint in checkpoints_to_be_deleted:
            logger.info("Deleting older checkpoint [{}] due to args.save_total_limit".format(checkpoint))
            #shutil.rmtree(checkpoint)
            self.smart_cleaner(checkpoint)
    def smart_cleaner(self,checkpoint_folder):
        NOT_DELETE_FILE_TYPES = [".txt" , ".json"  ,".bin"]
        NOT_DELETE_SPESIFIC_FILES = ["training_args.bin","scheduler.pt","config.json","sad2"] # You can also add folder name Example : "folder"    
        
        for filename in os.listdir(checkpoint_folder):
            full_path = os.path.join(checkpoint_folder,filename )
            extension = os.path.splitext(full_path)[1][1:]
            
            print(filename)
            if (not (filename in NOT_DELETE_SPESIFIC_FILES or extension  in NOT_DELETE_FILE_TYPES)):
                if (os.path.isdir(full_path)):
                    smart_cleaner(full_path)
                    print("Direct")
                else:
                    with open(full_path,"w") as f :
                        f.write(full_path+ " safetly deleted with smart cleaner")
                    print("[INFO] SAFETLY DELETE ACTIVE , File {} Deleted".format(full_path))
                    
