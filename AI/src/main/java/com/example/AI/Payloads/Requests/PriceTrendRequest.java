package com.example.AI.Payloads.Requests;

import lombok.AllArgsConstructor;
import lombok.Getter;

@AllArgsConstructor
@Getter
public class PriceTrendRequest {
    Double longitude;
    Double latitude;
    String location;
}
