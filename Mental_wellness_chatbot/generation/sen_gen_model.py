import torch
import torch.nn as nn

class EmotionConditionedSeq2Seq(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, emotion_dim, sos_id, eos_id, max_length=30):
        super(EmotionConditionedSeq2Seq, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.emotion_embedding = nn.Embedding(4, emotion_dim)
        self.encoder_lstm = nn.LSTM(embed_dim + emotion_dim, hidden_dim, batch_first=True)
        
        self.decoder_lstm = nn.LSTM(embed_dim + hidden_dim, hidden_dim, batch_first=True)
        self.fc_out = nn.Linear(hidden_dim, vocab_size)
        
        self.sos_id = sos_id
        self.eos_id = eos_id
        self.max_length = max_length
        
    def forward(self, src, emotion_label, tgt):
        e_embed = self.emotion_embedding(emotion_label).unsqueeze(1).repeat(1, src.shape[1], 1)
        src_embed = self.embedding(src)
        src_concat = torch.cat([src_embed, e_embed], dim=2)
        
        encoder_outputs, (h, c) = self.encoder_lstm(src_concat)
        
        tgt_embed = self.embedding(tgt)
        decoder_input = torch.cat([tgt_embed, encoder_outputs[:, -1:, :].repeat(1, tgt.shape[1], 1)], dim=2)
        decoder_outputs, _ = self.decoder_lstm(decoder_input, (h, c))
        
        logits = self.fc_out(decoder_outputs)
        return logits
    
    def generate(self, src, emotion_label, vocab, device):
        self.eval()
        with torch.no_grad():
            e_embed = self.emotion_embedding(emotion_label).unsqueeze(1).repeat(1, src.shape[1], 1)
            src_embed = self.embedding(src)
            src_concat = torch.cat([src_embed, e_embed], dim=2)
            
            encoder_outputs, (h, c) = self.encoder_lstm(src_concat)
            
            input_id = torch.tensor([[self.sos_id]], dtype=torch.long).to(device)
            generated = [self.sos_id]
            
            for _ in range(20):
                input_embed = self.embedding(input_id)
                decoder_input = torch.cat([input_embed, encoder_outputs[:, -1:, :]], dim=2)
                output, (h, c) = self.decoder_lstm(decoder_input, (h, c))
                logits = self.fc_out(output[:, -1, :])
                next_id = torch.argmax(torch.softmax(logits, dim=-1), dim=-1).item()
                
                if next_id == self.eos_id:
                    break
                
                generated.append(next_id)
                input_id = torch.tensor([[next_id]], dtype=torch.long).to(device)
            
            return generated
