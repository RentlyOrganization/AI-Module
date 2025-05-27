package com.example.AI.Payloads.Requests;

import lombok.AllArgsConstructor;
import lombok.Getter;

import java.math.BigDecimal;

@AllArgsConstructor
@Getter
public class PriceRateRequest {
    private BigDecimal price;
    Double longitude;
    Double latitude;
    String location;
    int rooms;
    float area;
}
