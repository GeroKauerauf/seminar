epochs = 15
history = model.fit(train_ds,
                    validation_data=val_ds,
                    epochs=epochs)