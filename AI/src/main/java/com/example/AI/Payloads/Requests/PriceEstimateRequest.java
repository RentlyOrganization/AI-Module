package com.example.AI.Payloads.Requests;

import lombok.AllArgsConstructor;
import lombok.Getter;

@AllArgsConstructor
@Getter
public class PriceEstimateRequest {
    Double longitude;
    Double latitude;
    String location;
    int rooms;
    float area;
}
